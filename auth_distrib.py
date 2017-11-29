import os
import math
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import sys
import MySQLdb
import numpy as np

assert len(sys.argv) ==3

datab= MySQLdb.connect(user = sys.argv[1], passwd= sys.argv[2],
        host='history-lab.org',db='declassification_frus')
c = datab.cursor()

c.execute("select name, count(*) as c From authorship group by name having c >= 50 order by c desc");
print(c.rowcount);

#get into a histogram
data = c.fetchall()
num_data = [rec[1] for rec in data]
mean = np.mean(num_data)
std_dev = np.std(num_data)

n, bins, patches = plt.hist(num_data, 40, facecolor='green', alpha=0.75)

# add a 'best fit' line
#y = mlab.normpdf( bins, mean_wlength, std_dev)
#l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('Word Length')
plt.ylabel('Occurence')
plt.title(r'$\mathrm{Histogram\ of\ Authors With Counts >= 50:}\ \mu=%f,\ \sigma=%f$'%(mean,std_dev))
plt.axis([min(num_data),max(num_data),0, 15])
plt.grid(True)

plt.savefig("./data/plots/AuthDist.png")
