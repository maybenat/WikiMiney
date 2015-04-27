Rails.application.routes.draw do
  # get 'welcome/index'

  root 'welcome#index'

  # pages with graphs
  get 'top' => 'welcome#top'
  get 'search' => 'welcome#search'
  get 'page_month' => 'welcome#page_month'
  get 'compare' => 'welcome#compare'
  get 'cluster' => 'welcome#cluster'
  get 'poster' => 'welcome#poster'

  # json responses
  # wikis
  get 'data/year/:year/month/:month/top/:size' => 'wikis#top'
  get 'data/project/:project/page/:page' => 'wikis#search', :constraints => { :project => /[^\/]+/, :page => /[^\/]+/ }
  get 'data/page/:page/year/:year/month/:month' => 'wikis#page_month'
  get 'data/compare/project/:project/page/:page' => 'wikis#compare', :constraints => { :project => /[^\/]+/, :page => /[^\/]+/ }

  # clusters
  get 'data/cluster/2008/october' => 'clusters#cluster'

  # Example of named route that can be invoked with purchase_url(id: product.id)
  #   get 'products/:id/purchase' => 'catalog#purchase', as: :purchase

  # basic resources
  resources :wikis  # comment out once above gets are set up correctly
  resources :clusters  # comment out once above gets are set up correctly
end
