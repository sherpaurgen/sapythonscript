#!/usr/bin/python3
'''
this script checks if there is Recv-Q or Send-Q on particular port number provided as arg to checkPort function.
if such queue is present then a message `ServiceQueueAlert Queue building up in port %s` is logged in /var/log/syslog
'''

import subprocess as sp
import logging
import sys
from time import sleep
import csv
logging.basicConfig(filename='/var/log/syslog',filemode='a',format='%(asctime)s - %(message)s',datefmt='%b %d %H:%M:%S', level=logging.WARN)

#with open('/tmp/trackQ.csv','w') as csvfh:
#    csvfh.write("proto,rq,sq,la,fa,st,pid\n")
    
#Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name

def checkPort(portnumber):
    with open('/tmp/trackQ.csv','w') as csvfh:
        csvfh.write("proto,rq,sq,la,fa,st,pid\n")
    count=0
    stat=0
    while count<11:
        with open('/tmp/trackQ.csv','a') as fout:
                proc1=sp.Popen(['netstat','-nap'],stdout=sp.PIPE)
                proc2=sp.Popen(['grep',':'+portnumber],stdin=proc1.stdout,stdout=sp.PIPE,stderr=sp.PIPE)
                proc3=sp.Popen(['sort', '-nk2'],stdin=proc2.stdout,stdout=sp.PIPE,stderr=sp.PIPE)
                proc4=sp.Popen(['tail','-n1'],stdin=proc3.stdout,stdout=sp.PIPE,stderr=sp.PIPE)
                proc1.stdout.close()
                proc2.stdout.close()
                proc3.stdout.close()
                out,err=proc4.communicate()
                with open('/tmp/err.txt','w+') as ferr:
                    if err:
                        ferr.write(err)
                        sys.exit("Error in communicate")
                stat1=out.decode().split()
                stat1=','.join(stat1)
                fout.write(stat1)
                fout.write("\n")
        sleep(1)
        count=count+1
    recvqueuesum=0
    sendqueuesum=0
    with open('/tmp/trackQ.csv','r') as rdfh:
        csv_file=csv.DictReader(rdfh)
        for row in csv_file:
            try:
                rq=dict(row)["rq"]
                sq=dict(row)["sq"]

                #if int(rq)>10000 or int(sq)>10000:
                #    stat=stat+1
                recvqueuesum=recvqueuesum+int(rq)
                sendqueuesum=sendqueuesum+int(sq)
            except Exception as e:
                logging.error('Error while parsing csv row-trackQ.csv',exc_info=True)
    if recvqueuesum/10>=10000 or sendqueuesum/10>=10000:
        logging.warning("LpQueueAlert Queue building up in port %s",portnumber)

def main():
    checkPort("5505")
    checkPort("5503")
if __name__ == "__main__":
    main() 
