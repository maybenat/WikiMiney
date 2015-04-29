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
    "Undefined",
    "undefined",
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


  # just a helper method for parsing json
  # PS: This is hideous
  def json_strip_views(json, month_param, year_param)
    ini_hash = JSON.parse(json)
    ret_hash = []

    # God, this is so ugly... I'm ashamed. I'm so sorry...
    ini_hash.each do |page|
      wvs = []
      page["wikiviews"].each do |view|
        if view["month"] == month_param && view["year"] == year_param
          wvs.push(view)
        end
      end
      ret_hash.push({"project" => page["project"], "page" => page["page"], "wikiviews" => wvs})
    end
    ret_json = ret_hash.to_json
    return ret_json
  end


  # get 'data/year/:year/month/:month/top/:size' => 'wikis#top'
  # change to top_month and fix url -> 'data/top/year/month'

  # Okay, so here's what's going on:
  #   I want the top <size> pages in a specific month and year. After the ActiveRecord .where() call, @wikis contains
  #   all of the correct pages. But I also want the information in the wikiviews table to be included in the returned
  #   json. The problem is that the to_json() call finds *all* of the associated wikiviews for each page, even the ones
  #   outside of the month and year constraints. So to_json() gets all of the information we want (plus a little extra)
  #   and then I loop through that json hash and strip out all of the uneccessary data.
  def top #_month
    size = params[:size].to_i
    if size > 70
      size = 70
    end
    @wikis = Wiki.joins(:wikiviews).where("year = ? AND month = ? AND day = 'all' AND page NOT IN (?)",
            params[:year], params[:month], $special_exclude_list).distinct.order('views DESC, page').take(size)
    json = @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
    ret_json = json_strip_views(json, params[:month], params[:year])
    render :json => ret_json
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
  # look at comment for top_month for what's going on
  def page_month
    @wikis = Wiki.joins(:wikiviews).where("page = ? AND month = ? AND year = ?", params[:page], params[:month], params[:year]).distinct
    json = @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
    ret_json = json_strip_views(json, params[:month], params[:year])
    render :json => ret_json
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
