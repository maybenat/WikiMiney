class WikisController < ApplicationController
  def index
    #@wikis = Wiki.where("project = ?", "en").take(50)
    @wikis = Wiki.joins(:wikiviews).order('views DESC, page').take(25)
  end

  def show
    @wiki = Wiki.find(params[:id])
  end

  # get 'data/year/:year/month/:month/top/:size' => 'wikis#top'
  def top
    size = params[:size].to_i
    if size > 50
      size = 50
    end
    @wikis = Wiki.joins(:wikiviews).where("year = ? AND month = ?", params[:year], params[:month]).order('views DESC, page').take(size)
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end

  # get 'data/page/:page' => 'wikis#search'
  def search
    @wikis = Wiki.where("page = ?", params[:page])
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end

  # get 'data/page/:page/year/:year/month/:month' => 'wikis#page_month'
  def page_month
    @wikis = Wiki.joins(:wikiviews).where("page = ? AND year = ? AND month = ?", params[:page], params[:year], params[:month])
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end

  # get 'data/cluster/2008/october' => 'wikis#cluster'
  def cluster
    @wikis = Wiki.joins(:wikiviews).where("year = '2008' AND month = '10' AND day = 'all'")
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end
end
