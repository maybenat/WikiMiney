# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).

paths = [
  "db/data/2008/10/ready-for-db/",
  "db/data/2008/11/ready-for-db/",
  "db/data/2008/12/ready-for-db/",
  "db/data/2012/10/ready-for-db/",
  "db/data/2012/11/ready-for-db/",
  "db/data/2012/12/ready-for-db/"
]

paths.each do |path|
  Dir.foreach(path) do |item|
    if item[0, 13] == "stripped-agg-" 
      year = path.split('/')[2]
      month = path.split('/')[3]
      if item[0, 17] == "stripped-agg-day-"
        day = item[17, 19]
      else
        day = "all"
      end
      input = File.open(path + item)
      puts "Starting %s/%s/%s - %s" % [month, day, year, path + item]
      input.each_line do |line|
        line = line[0, line.length - 1].split(' ')
        view = line[2].to_i
        byte = line[3].to_i
        wiki = Wiki.find_or_create_by(:project => line[0], :page => line[1])
        wiki.wikiviews.create(:year => year, :month => month, :day => day, :views => view, :bytes => byte)
      end
    end
  end
end


#input = File.open('db/data/2008/10/stripped-agg-cluster')
#input.each_line do |line|
#  l = line[0, line.length - 1].split(' ')
#  view = l[2].to_i
#  byte = l[3].to_i
#  Cluster.create(:project => l[0], :page => l[1], :year => "2008", :month => "10", :views => view, :bytes => byte, :cluster => l[4])
#end
