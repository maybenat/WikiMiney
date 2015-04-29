class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  protect_from_forgery with: :exception

  # list of pages to not include in returned json
  $special_exclude_list = [
    "Special:AutoLogin",
    "Special:Search",
    "Special:Random",
    "Special:Randompage",
    "Special:Watchlist",
    "Special:Export",
    "Main_Page",
    "MainPage",
    "index.html",
    "Wiki",
    "HIT%20MUSIC%20ONLY",
    "favicon.ico",
    "Favicon.ico",
    "favicon.gif",
    "Favicon.gif",
    "en",
    "Wsearch.php",
    "index.php",
    "/Talk:Main_Page",
    "Undefined",
    "undefined",
    "/Wikipedia:Your_first_article",
    "File:Marvel_1602.jpg",
    "File:Beograd_7642.jpg",
    "Wiktionary:Main_Pag%12",
    "Wiktionary:Main_Pag%04",
    "%5Bobject_Object%5D",
    "Main_Page/",
    "500.shtml"
  ]

  # just a helper method for parsing json
  # takes json and strips out the unrequested months
  # and years from the result and returns json
  # PS: This is hideous
  def json_strip_views(json, month_param, year_param)
    ini_hash = JSON.parse(json)
    ret_hash = []

    # God, this is so ugly... I'm ashamed. I'm so sorry...
    ini_hash.each do |page|
      wvs = []
      page["wikiviews"].each do |view|
        if month_param.nil? && view["year"] == year_param
          wvs.push(view)
        elsif view["month"] == month_param && view["year"] == year_param
          wvs.push(view)
        end
      end
      ret_hash.push({"project" => page["project"], "page" => page["page"], "wikiviews" => wvs})
    end
    ret_json = ret_hash.to_json
    return ret_json
  end
end
