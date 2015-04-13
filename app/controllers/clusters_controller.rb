class ClustersController < ApplicationController
  def index
    @clusters = Cluster.take(50)
  end

  ## get 'data/cluster/2008/october' => 'wikis#cluster'
  #def cluster
  #  @wikis = Wiki.joins(:wikiviews).where("year = '2008' AND month = '10' AND day = 'all'")
  #  render :json => @wikis.to_json(:only => [:project, :page], :include => {:wikiviews => {:only => [:year, :month, :day, :views, :bytes]}})
  #end
end
