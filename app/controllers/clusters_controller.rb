class ClustersController < ApplicationController
  def index
    @clusters = Cluster.all
  end
end
