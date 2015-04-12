namespace :init do
  desc "Adds entries from text files to database"
  task :add_wikis => :environment do
    path = 'lib/tasks/data/2008/10/'
    Dir.foreach(path) do |item|
      if item[0, 17] == "stripped-agg-day-"
        @input = File.open(path + item)
        day = item[17, 19]
        puts "Starting day " + day
        @input.each_line do |line|
          line = line[0, line.length - 1].split(' ')
          view = line[2].to_i
          byte = line[3].to_i
          wiki = Wiki.find_or_create_by(:project => line[0], :page => line[1])
          wiki.wikiviews.create(:year => "2008", :month => "10", :day => day, :views => view, :bytes => byte)
        end
      end
    end
  end
end
