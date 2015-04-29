class TopController < ApplicationController
  # Okay, so here's what's going on:
  #   I want the top <size> pages in a specific month and year. After the ActiveRecord .where() call, @wikis contains
  #   all of the correct pages. But I also want the information in the wikiviews table to be included in the returned
  #   json. The problem is that the to_json() call finds *all* of the associated wikiviews for each page, even the ones
  #   outside of the month and year constraints. So to_json() gets all of the information we want (plus a little extra)
  #   and then I loop through that json hash and strip out all of the uneccessary data.
  # get 'data/top/:size/year/:year/month/:month' => 'top#month'
  def month
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

  # get 'data/top/:size/year/:year' => 'top#year'
  def year
    size = params[:size].to_i
    if size > 70
      size = 70
    end
    @wikis = Wiki.joins(:wikiviews).where("year = ? AND day = 'all' AND page NOT IN (?)",
            params[:year], $special_exclude_list).distinct.order('views DESC, page').take(size)
    json = @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
    ret_json = json_strip_views(json, nil, params[:year])
    render :json => ret_json
  end

  # get 'data/progress/mobile' => 'top#mobile'
  def mobile
    @mobiles = Wiki.joins(:wikiviews).where("project = 'en.mw'").distinct
    render :json => @mobiles.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  end
end
