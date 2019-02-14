import ipinfo
import csv
import config

access_token = config.apikey

outputcsv = open('output.csv', 'wb')    
outputWriter = csv.writer(outputcsv)

#<!--Write CSV Table Headers--!>
outputWriter.writerow(['IPADDRESS','LOCATION','CITY','REGION','COUNTRY','ORGANIZATION'])

#<!--Call Api methods--!>
handler = ipinfo.getHandler(access_token)
with open('listofipaddresses.txt', 'r') as listofipAddresses:
    for ipAddress in listofipAddresses:
        details = handler.getDetails(ipAddress)
        outputWriter.writerow([details.ip,details.loc,details.city,details.region,details.country,details.org])
