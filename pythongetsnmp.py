python get snmp data from OLT
#!/usr/bin/python
#olt_snmp.py <olt> <snmp community> <ontid>
import sys
import subprocess
OLT=sys.argv[1]
ONT=sys.argv[2]
COMM="aaaabbbb83gddee2"
SNMPWALK="/usr/bin/snmpwalk"
uploadtree=".1.3.6.1.4.1.2011.6.128.1.1.4.23.1.3."+ONT
downloadtree=".1.3.6.1.4.1.2011.6.128.1.1.4.23.1.4."+ONT

UPLOAD=subprocess.check_output([SNMPWALK,"-v2c","-c",COMM,OLT,uploadtree])
DOWNLOAD=subprocess.check_output([SNMPWALK,"-v2c","-c",COMM,OLT,downloadtree])

uploadrate=UPLOAD.split()
downloadrate=DOWNLOAD.split()
print "in_traffic:{} out_traffic:{}" .format(uploadrate[3],downloadrate[3])



# to run the script
 python /usr/local/cacti/scripts/olt_snmp.py 100.126.25.6 4194306816.0


# snmpwalk output unfiltered is like below

SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194305792.0 = Counter64: 3416502644
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194305792.1 = Counter64: 13464627881
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194305792.2 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194305792.3 = Counter64: 4940907783
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194305792.4 = Counter64: 551442
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194305792.5 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194305792.6 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194305792.7 = Counter64: 2867386967
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194305792.8 = Counter64: 10518683172
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194305792.9 = Counter64: 853060354
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306048.0 = Counter64: 517092232010
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306048.1 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306048.2 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306048.3 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306048.4 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306048.5 = Counter64: 34863677601
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306048.6 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306048.7 = Counter64: 8248385809
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306048.8 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306048.9 = Counter64: 30703789772
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306048.10 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306048.11 = Counter64: 191145018
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306560.0 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306560.1 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306560.2 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306560.3 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306816.0 = Counter64: 14006587616
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306816.1 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306816.2 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306816.3 = Counter64: 5269993683
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306816.4 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194306816.5 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194307072.0 = Counter64: 34861334763
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194307328.0 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194307328.1 = Counter64: 0
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194307328.2 = Counter64: 2572949148
SNMPv2-SMI::enterprises.2011.6.128.1.1.4.23.1.3.4194307840.0 = Counter64: 9045396
