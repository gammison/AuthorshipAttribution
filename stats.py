import os
import math
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
dir = '../docs/SiscoDocs'

mean_char_mark= 1
mean_char= 0
mean_wlength = 0
mean_wmark = 1
mean_line_num=0
mean_line_count=1
std_dev = 0
max_w = 0
min_w=100000000
std_dev_w = 0
data = []
for filename in os.listdir(dir):
    tdoc = open(dir+'/'+filename,'r')
    avg_n_c=0
    avg_n_w=0
    print(filename)
    for line in tdoc.readlines():
        for x in line:
            avg_n_c+=1
        avg_n_w+=len(line.split(' '))
            
    mean_char= ((mean_char*mean_char_mark)+avg_n_c)/(mean_char_mark+1)
    mean_char_mark+=1
    mean_wlength = ((mean_wlength*mean_wmark)+avg_n_w)/(mean_wmark+1)
    mean_wmark+=1
    data.append(avg_n_w)
    print(avg_n_c,avg_n_w)
    min_w = min(min_w,avg_n_w)
    max_w=max(max_w,avg_n_w)
    tdoc.close()
print("mean char length:",mean_char)
print("mean word length:", mean_wlength)
print("min word:",min_w)
print("max word:",max_w)
for x in data:
    std_dev += math.pow((x-mean_wlength),2)
std_dev = math.sqrt(std_dev)/mean_wlength
print("standard deviation:",std_dev)

"""n, bins, patches = plt.hist(data, 30, facecolor='green', alpha=0.75)

# add a 'best fit' line
#y = mlab.normpdf( bins, mean_wlength, std_dev)
#l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('Word Length')
plt.ylabel('Occurence')
plt.title(r'$\mathrm{Histogram\ of\ Newsom:}\ \mu=%f,\ \sigma=%f$'%(mean_wlength,std_dev))
plt.axis([min_w,max_w,0, 40])
plt.grid(True)

plt.savefig("../plots/Newsom.png")"""
