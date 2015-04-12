namespace :cluster do
  desc "Adds month data from text file to cluster table"
  task :add_cluster => :environment do
    @input = File.open('./data/2008/10/stripped-agg-cluster')
    @input.each_line do |line|
      line = line[0, line.length - 1].split(' ')
      proj = line[0]
      page = line[1]
      view = line[2].to_i
      byte = line[3].to_i
      clus = line[4]
      Cluster.create(:project => proj, :page => page, :year => "2008", :month => "10", :views => view, :bytes => byte, :cluster => clus)
    end
  end
end
