import os


for fn in os.listdir('.'): # loop through all files
  if os.path.isfile(fn) and fn[:13] == "stripped-agg-": # only care about non-directories that begin with 'en-'
    p = "ready-for-db/"
    if not os.path.isdir(p):
      os.system("mkdir %s" % p)
    day = "all"
    stripped = "stripped-agg-%s-days" % day
    if fn[:17] == "stripped-agg-day-":
      day = fn[17:19]
      stripped = "stripped-agg-day-%s" % day
    if not os.path.isfile(p + stripped):
      print "stripping %s to %s" % (stripped, p + stripped)
      day = open("%s" % stripped, "r")
      strip = open(p + stripped, "w")
      for line in day:
        views = int(line[:-1].split(' ')[2])
        if views >= 5000: 
          strip.write(line)
      strip.close()
      day.close()
