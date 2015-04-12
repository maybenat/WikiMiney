class WikisController < ApplicationController
  def index
    @wikis = Wiki.where("project = ?", "en").take(50)
  end

  def show
    @wiki = Wiki.find(params[:id])
  end

  # get 'data/year/:year/month/:month/top/:size' => 'wikis#top'
  def top
    @wikis = Wiki.includes(:wikiviews).where("year = ? AND month = ? AND views > ?", params[:year], params[:month], params[:size].to_i).take(params[:size].to_i)
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end

  # get 'data/page/:page' => 'wikis#search'
  def search
    @wikis = Wiki.where("page = ?", params[:page])
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end

  # get 'data/page/:page/year/:year/month/:month' => 'wikis#page_month'
  def page_month
    @wikis = Wiki.find(params[:id])
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end

  # get 'data/cluster/2008/october' => 'wikis#cluster'
  def cluster
    @wikis = Wiki.find(params[:id])
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end
end
