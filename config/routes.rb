Rails.application.routes.draw do
  root 'welcome#index'

  # pages with graphs
  get 'top' => 'welcome#top'
  get 'compare' => 'welcome#compare'
  get 'cluster' => 'welcome#cluster'
  get 'search' => 'welcome#search'
  get 'poster' => 'welcome#poster'
  get 'about' => 'welcome#about'
  get 'mobile' => 'welcome#mobile'

  # json responses
  get 'data/top/:size/year/:year' => 'top#year'
  get 'data/top/:size/year/:year/month/:month' => 'top#month'

  get 'data/progress/mobile' => 'top#mobile'
  get 'data/cluster/2008/october' => 'clusters#cluster'

  get 'data/search/page/:page' => 'search#page', :constraints => { :page => /[^\/]+/ }
  get 'data/search/project/:project/page/:page' => 'search#search', :constraints => { :project => /[^\/]+/, :page => /[^\/]+/ }
  get 'data/search/project/:project/page/:page/year/:year' => 'search#page_year', :constraints => { :project => /[^\/]+/, :page => /[^\/]+/ }
  get 'data/search/project/:project/page/:page/year/:year/month/:month' => 'search#page_month', :constraints => { :project => /[^\/]+/, :page => /[^\/]+/ }

  # basic resources
  # resources :wikis  # comment out once above gets are set up correctly
  # resources :clusters  # comment out once above gets are set up correctly
end
