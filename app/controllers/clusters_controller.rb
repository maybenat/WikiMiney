class ClustersController < ApplicationController
  # get 'data/cluster/2008/october' => 'cluster#cluster'
  def cluster
    @cluster = Cluster.where("year = '2008' AND month = '10'")
    render :json => @cluster.to_json(:only => [:project, :page, :views, :bytes, :cluster])
  end
end
