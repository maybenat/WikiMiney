from __future__ import with_statement
import os
import sqlite3

for fn in os.listdir('.'): # loop through all files
  if os.path.isfile(fn) and fn[:3] == "en-": # only care about non-directories that begin with en-
    existed = False
    day_name = fn[20:22] # get day of file
    if os.path.isfile("day-%s.db" % day_name):
      existed = True # see if the day file already existed
    con = sqlite3.connect("day-%s.db" % day_name) # connect to existing db or make new one
    con.text_factory = str
    c = con.cursor()
    day = open(fn, "r")
    if not existed: # this is the first hour of a day
      print "day %s" % day_name 
      c.execute('''CREATE TABLE day (project TEXT, page TEXT, views INT, bytes INT)''')
      for line in day: # insert all values into new table
        e = line[:-1].split(" ") # [project, page, views, bytes]
        if int(e[2]) >= 100:
          c.execute("INSERT INTO day VALUES (?, ?, ?, ?)", (e[0], e[1], int(e[2]), int(e[3])))
    else: # this is any other hour than the first in a day
      print fn
      for line in day: # add all values to existing day table
        e = line[:-1].split(" ") # [project, page, views, bytes]
        if int(e[2]) >= 100:
          c.execute("SELECT views, bytes FROM day WHERE project=? AND page=?", (e[0], e[1]))
          vb = c.fetchone()
          if vb: # the entry already exists, add to existing page views and bytes
            c.execute("UPDATE day SET views=?, bytes=? WHERE project=? AND page=?", (vb[0] + int(e[2]), vb[1] + int(e[3]), e[0], e[1]))
          else: # entry doesn't already exist and must be added
            c.execute("INSERT INTO day VALUES (?, ?, ?, ?)", (e[0], e[1], int(e[2]), int(e[3])))
    day.close()
    con.commit()
    con.close()
