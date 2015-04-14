# WikiMiney
This is the repository for the [CS 5140 Data Mining](http://www.cs.utah.edu/~jeffp/teaching/cs5140.html)
final project at The University of Utah. We are analyzing Wikipedia page view statistics and are building
an interactive site with a series of graphs and charts the help visualize this massive collection of
data. We soon hope to have the site up and running with AWS [here](#).


### Dependencies
* [RVM](http://rvm.io)


### Getting This Rails App Running Locally
Processing all of the data has taken enormous effort. We currently have a directory of preprocessed data
sitting in a directory on AWS.

```
git clone https://github.com/nataliemcmullen/WikiMiney.git wikiminey
cd wikiminey
rvm use --create --rvmrc 2.2@wikiminey
rvm rvmrc warning ignore '/path/to/wikiminey/.rvmrc'
bundle install
```

If you have access to our AWS account just do

```
rake db:create
rake db:migrate
scp <aws_ip>:sqlite_snapshots/<x>.sqlite3 db/development.sqlite3
rails server
```

Otherwise,
Follow instructions in [Data Download](DATA_DL.md). This will take a LONG time to get actual data.
The rake db:setup command will take a long time to populate the database if you followed the scripts in the
Data Download wiki for all six months

```
rake db:migrate
rake db:setup
rails server
```

Go to localhost:3000 to see some stuff


### Useful Links
* [Wikimedia Dumps](http://dumps.wikimedia.org/other/pagecounts-raw)
* [Wikimedia Help](http://wikitech.wikimedia.org/wiki/Analytics/Data/Pagecounts-raw)
* [Rails Getting Started](http://guides.rubyonrails.org/getting_started.html)
* [Remaining TODO Development](TODO.md)
* [Highcharts-rails](http://github.com/PerfectlyNormal/highcharts-rails)
* [Bootstrap-rails](https://github.com/seyhunak/twitter-bootstrap-rails)
* [Deploy Rails to AWS](http://dennissuratna.com/rails-deployment-aws1)
* [AWS ELB Docs](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Ruby_rails.html)


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
