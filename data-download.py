#coding=utf-8
import os,urllib2,re


aStr="https://commondatastorage.googleapis.com/clusterdata-2011-2/task_events/part-"
bStr="-of-00500.csv.gz"
if(not os.path.exists(r'download/') ):
    os.mkdir(r'download/')

for i in range(500):
    furl=aStr+ ("%05d" % i)+bStr

    print(furl)
                
    fname="download/"+ "part-" + ("%05d" % i) + bStr 
    data = urllib2.urlopen(furl).read()
    with open(fname, 'wb') as f:
        f.write(data)
print("下载完成！")
os.system('pause')
