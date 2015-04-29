class WikisController < ApplicationController
  $special_exclude_list = [
    "Special:AutoLogin",
    "Special:Search",
    "Special:Random",
    "Special:Randompage",
    "Special:Watchlist",
    "Special:Export",
    "Main_Page",
    "MainPage",
    "index.html",
    "Wiki",
    "HIT%20MUSIC%20ONLY",
    "favicon.ico",
    "Favicon.ico",
    "favicon.gif",
    "Favicon.gif",
    "en",
    "Wsearch.php",
    "index.php",
    "/Talk:Main_Page",
  ]

  def index
    @wikis = Wiki.joins(:wikiviews).where("day = 'all' AND page NOT IN (?)", $special_exclude_list).order('views DESC, page').distinct.take(25)
  end

  def show
    @wiki = Wiki.find(params[:id])
    if @wiki.project == "en"
      @project = "en.wikipedia"
    elsif @wiki.project == "en.b"
      @project = "en.wikibooks"
    elsif @wiki.project == "en.d"
      @project = "en.wiktionary"
    elsif @wiki.project == "en.f"
      @project = "en.wikimediafoundation"
    elsif @wiki.project == "en.m"
      @project = "en.wikimedia"
    elsif @wiki.project == "en.n"
      @project = "en.wikinews"
    elsif @wiki.project == "en.q"
      @project = "en.wikiquote"
    elsif @wiki.project == "en.s"
      @project = "en.wikisource"
    elsif @wiki.project == "en.v"
      @project = "en.wikiversity"
    elsif @wiki.project == "en.voy"
      @project = "en.wikivoyage"
    elsif @wiki.project == "en.w"
      @project = "en.mediawiki"
    elsif @wiki.project == "en.wd"
      @project = "en.wikidata"
    else
      @project = "en.wikipedia"
    end
  end

  # get 'data/year/:year/month/:month/top/:size' => 'wikis#top'
  # change to top_month and fix url -> 'data/top/year/month'
  def top
    size = params[:size].to_i
    if size > 70
      size = 70
    end
    @wikis = Wiki.find_by_sql ["SELECT * FROM wikis INNER JOIN wikiviews ON wikiviews.wiki_id = wikis.id
                                WHERE wikiviews.month = ? AND wikiviews.year = ? AND wikis.page NOT IN (?)
                                ORDER BY wikiviews.views DESC LIMIT ?",
                                params[:month], params[:year], $special_exclude_list, size]
    render :json => @wikis.to_json(:only => [:project, :page, :year, :month, :day, :views, :bytes])
  end

  # add a top_year -> 'data/top/year'

  # get 'data/project/:project/page/:page' => 'wikis#search'
  # change to search_page
  def search
    @wikis = Wiki.where("project = ? AND page = ?", params[:project], params[:page])
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end

  # get 'data/page/:page/year/:year/month/:month' => 'wikis#page_month'
  # change to search_page_month
  def page_month
    @wikis = Wiki.find_by_sql ["select * from wikis inner join wikiviews on wikiviews.wiki_id = wikis.id
                                where wikis.page = ? AND wikiviews.month = ? AND wikiviews.year = ?",
                                params[:page], params[:month], params[:year]]
    render :json => @wikis.to_json(:only => [:project, :page, :year, :month, :day, :views, :bytes])
  end

  # get 'data/compare/project/:project/page/:page' => 'wikis#compare'
  # DONT NEED. Just make two calls to page_month
  def compare
    @wikis = Wiki.where("project = ? AND page = ?", params[:project], params[:page])
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end

  # add uri comment
  def mobile
    @mobiles = Wiki.joins(:wikiviews).where("project = 'en.mw'").distinct
    render :json => @mobiles.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end
end
