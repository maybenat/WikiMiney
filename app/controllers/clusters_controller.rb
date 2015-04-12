class ClustersController < ApplicationController
  def index
    @clusters = Cluster.take(50)
  end
end
