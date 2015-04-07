# WikiMiney
This is the repository for the [CS 5140 Data Mining](http://www.cs.utah.edu/~jeffp/teaching/cs5140.html)
final project at The University of Utah. We are analyzing Wikipedia page view statistics and are building
an interactive site with a series of graphs and charts the help visualize this massive collection of
data. We soon hope to have the site up and running with AWS [here](#).


### Dependencies
* [RVM](http://rvm.io)


### Getting This Rails App Running Locally

```
git clone https://github.com/nataliemcmullen/WikiMiney.git wikiminey
cd wikiminey
rvm use --create --rvmrc 2.2@wikiminey
rvm rvmrc warning ignore '/path/to/wikiminey/.rvmrc'
bundle install
rake db:create
rake db:migrate
rails server
```
Go to localhost:3000 to see some stuff


### Useful Links
* [Wikimedia Dumps](http://dumps.wikimedia.org/other/pagecounts-raw)
* [Wikimedia Help](http://wikitech.wikimedia.org/wiki/Analytics/Data/Pagecounts-raw)
* [Rails Getting Started](http://guides.rubyonrails.org/getting_started.html)
* [Rails Model](http://guides.rubyonrails.org/active_record_basics.html)


### Authors
* [Natalie McMullen](http://github.com/nataliemcmullen)
* [Sam Olds](http://github.com/samolds)


### Reviews
"An interactive... WikiMiney."
* Natalie McMullen

"No Results for WikiMiney... Check the spelling or try alternate spellings."
* Yelp

"Did you mean:  wikimini   wikiminer   wiki money   wiki mine"
* Google
