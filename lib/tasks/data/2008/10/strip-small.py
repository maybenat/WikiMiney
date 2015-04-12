import os


for fn in os.listdir('.'): # loop through all files
  if os.path.isfile(fn) and fn[:4] == "agg-": # only care about non-directories that begin with 'en-'
    stripped = "stripped-%s" % fn
    if not os.path.isfile(stripped):
      print "stripping %s to %s" % (fn, stripped)
      day = open(fn, "r")
      strip = open(stripped, "w")
      for line in day:
        views = int(line[:-1].split(' ')[2])
        if views >= 20: 
          strip.write(line)
      strip.close()
      day.close()
