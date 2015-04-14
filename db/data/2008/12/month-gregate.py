import os


class ReadFileQueue:
  def __init__(self, name, type):
    self.file = open(name, type)
    self.cur_line = self.file.readline()

  def peek(self):
    return self.cur_line

  def pop(self):
    result = self.cur_line
    self.cur_line = self.file.readline()
    return result

  def close(self):
    return self.file.close()



for fn in os.listdir('.'): # loop through all files
  if os.path.isfile(fn) and fn[:17] == "stripped-agg-day-": # only care about non-directories that begin with 'stripped-agg-day-'
    agg_name = "stripped-agg-all-days"
    if os.path.isfile(agg_name):
      print "\taggregating %s with %s" % (fn, agg_name)
      day = ReadFileQueue(fn, "r")
      os.system("mv %s %s.temp" % (agg_name, agg_name))
      old_agg = ReadFileQueue(agg_name + ".temp", "r")
      new_agg = open(agg_name, "w")

      while day.peek() or old_agg.peek():
        d_line = day.peek()
        d = d_line[:-1].split(' ')
        da = ''
        if len(d) == 4:
          da = d[0] + "-" + d[1]  # 'project-page_name'

        a_line = old_agg.peek()
        a = a_line[:-1].split(' ')
        ag = ''
        if len(a) == 4:
          ag = a[0] + "-" + a[1]  # 'project-page_name'

        if ag and da:
          if a[0] == "en" and d[0] != "en":
            day.pop()
            line = "%s" % d_line
          elif a[0] != "en" and d[0] == "en":
            old_agg.pop()
            line = "%s" % a_line
          elif d[0] == a[0]:
            if d[1] == a[1]:  # same exact page
              old_agg.pop()
              day.pop()
              view = int(a[2]) + int(d[2])
              byte = int(a[3]) + int(d[3])
              line = "%s %s %d %d\n" % (a[0], a[1], view, byte)
            elif a[1] > d[1]:  # old_agg queue is ahead of day queue
              day.pop()
              line = "%s" % d_line
            else:  # old_agg queue is behind day queuee
              old_agg.pop()
              line = "%s" % a_line
          elif a[0] > d[0]:  # old_agg queue is ahead of day queue
            day.pop()
            line = "%s" % d_line
          else:  # old_agg queue is behind day queuee
            old_agg.pop()
            line = "%s" % a_line
        elif ag:
          old_agg.pop()
          line = "%s" % a_line
        else:
          day.pop()
          line = "%s" % d_line

        new_agg.write(line)

      day.close()
      new_agg.close()
      old_agg.close()
      os.system("rm %s.temp" % agg_name)
    else:
      print "initializing %s with %s" % (agg_name, fn)
      day = open(fn, "r")
      new_agg = open(agg_name, "w")
      for line in day:
        new_agg.write(line)
      new_agg.close()
      day.close()
