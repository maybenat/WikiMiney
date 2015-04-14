# Data Download
There were a handful of scripts written to download the data, process it, strip it down,
and get it into a manageable format to work with this app. The data all came from the 
[Wikimedia Dumps](http://dumps.wikimedia.org/other/pagecounts-raw). More information
can be found [here](http://wikitech.wikimedia.org/wiki/Analytics/Data/Pagecounts-raw).
We selected six months to process October, November, and December of 2008 and 2012.



### Overview
* Data downloaded in its entirety
* Data uncompressed of the gzip format
* Data stripped of everything except for English projects
* Data aggregated from hourly files to daily files
* Data stripped of everything with less than 20 views per day
* Data aggregated to additional monthly file
* Data stripped of everything with less than 5000 views
* Final data files added to ready-for-db/ directories for each month



### To Execute
The following scripts need to be executed in this exact order. The final text files
will be located in an inner ready-for-db/ directory. Each set of scripts can be found
in db/data/*year*/*month*.
When rake:seed is called, the files within db/data/*year*/*month*/ready-for-db will be
added to a SQLite3 database

Note: This will seriously take weeks and about 1.3TB, initially. Be prepared.

```
cd db/data/<year>/<month>/
python get_gzs.py
python process.py
python queue-gregate.py
python strip-small.py
python month-gregate.py
python prep-for-db.py
```
