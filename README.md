# WikiMiney
This is the repository for the [CS 5140 Data Mining](http://www.cs.utah.edu/~jeffp/teaching/cs5140.html)
final project at The University of Utah. We are analyzing Wikipedia page view statistics and are building
an interactive site with a series of graphs and charts the help visualize this massive collection of
data. We soon hope to have the site up and running with AWS [here](#).


### Dependencies
* [RVM](http://rvm.io)
* [Wikimedia Dumps](http://dumps.wikimedia.org/other/pagecounts-raw)


### Getting This Rails App Running Locally
Processing all of the data has taken enormous effort. We currently have a directory of processed data
sitting in a directory on AWS. In the steps below, the directory copied to wikiminey/lib/tasks/data is
expected to contain everything.

```
git clone https://github.com/nataliemcmullen/WikiMiney.git wikiminey
cp -r data wikiminey/lib/tasks/data
cd wikiminey
rvm use --create --rvmrc 2.2@wikiminey
rvm rvmrc warning ignore '/path/to/wikiminey/.rvmrc'
bundle install
rake db:create
rake db:migrate
rake init:add_wikis
rake init:add_cluster
rails server
```
The rake init:add_wikis command will take a long time to populate the database
Go to localhost:3000 to see some stuff


### Useful Links
* [Wikimedia Help](http://wikitech.wikimedia.org/wiki/Analytics/Data/Pagecounts-raw)
* [Rails Getting Started](http://guides.rubyonrails.org/getting_started.html)
* [Remaining TODO Development](TODO.md)


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
