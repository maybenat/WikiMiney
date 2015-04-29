class SearchController < ApplicationController
  # get 'data/search/page/:page' => 'search#page'
  def page
    @wikis = Wiki.where("page = ?", params[:page])
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end

  # get 'data/search/project/:project/page/:page' => 'search#search'
  def search
    @wikis = Wiki.where("project = ? AND page = ?", params[:project], params[:page])
    render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end

  # look at comment for top#month for what's going on
  # get 'data/search/project/:project/page/:page/year/:year' => 'search#page_year'
  def page_year
    @wikis = Wiki.joins(:wikiviews).where("project = ? AND page = ? AND year = ?", params[:project], params[:page], params[:year]).distinct
    json = @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
    ret_json = json_strip_views(json, nil, params[:year])
    render :json => ret_json
  end

  # look at comment for top#month for what's going on
  # get 'data/search/project/:project/page/:page/year/:year/month/:month' => 'search#page_month'
  def page_month
    @wikis = Wiki.joins(:wikiviews).where("project = ? AND page = ? AND month = ? AND year = ?", params[:project], params[:page], params[:month], params[:year]).distinct
    json = @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
    ret_json = json_strip_views(json, params[:month], params[:year])
    render :json => ret_json
  end
end
