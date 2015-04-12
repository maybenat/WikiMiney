namespace :init_db do
  desc "Adds entries from text files to database"
  task :add_wikis => :environment do
    Dir.foreach('./data/2008/10') do |item|
      if item[0, 17] == "stripped-agg-day-"
        @input = File.open(item)
        day = item[17, 19]
        @input.each_line do |line|
          line = line[0, line.length - 1].split(' ')
          proj = line[0]
          page = line[1]
          view = line[2].to_i
          byte = line[3].to_i
          wiki = Wiki.find_by(:project => proj, :page => page)
          if !wiki
            wiki = Wiki.create(:project => proj, :page => page)
          end
          wiki.wikiviews.create(:year => "2008", :month => "10", :day => day, :views => view, :bytes => byte)
        end
      end
    end
  end
end
