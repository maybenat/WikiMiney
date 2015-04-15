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
  def top
    size = params[:size].to_i
    if size > 70
      size = 70
    end
    #@wikis = Wiki.joins(:wikiviews).where("year = ? AND month = ? AND day = 'all'", params[:year], params[:month]).order('views DESC, page').take(size)
    @wikis = Wiki.joins(:wikiviews).where("year = ? AND month = ? AND page NOT IN (?)", params[:year], params[:month], $special_exclude_list).distinct.order('views DESC, page').take(size)
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end

  # get 'data/project/:project/page/:page' => 'wikis#search'
  def search
    @wikis = Wiki.where("project = ? AND page = ?", params[:project], params[:page])
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end

  # get 'data/page/:page/year/:year/month/:month' => 'wikis#page_month'
  def page_month
    @wikis = Wiki.joins(:wikiviews).where("page = ? AND year = ? AND month = ?", params[:page], params[:year], params[:month]).distinct
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end

  # get 'data/cluster/2008/october' => 'wikis#cluster'
  def cluster
    @wikis = Wiki.joins(:wikiviews).where("year = '2008' AND month = '10' AND day = 'all' AND page NOT IN (?)", $special_exclude_list).distinct
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end
end
