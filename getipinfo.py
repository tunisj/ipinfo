import ipinfo
import sys
import csv
import os
import argparse
import config

access_token = config.apikey

class getipinfo:
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def main(self):
        outputcsv = open(self.output, 'wb')    
        outputWriter = csv.writer(outputcsv)
        outputWriter.writerow(['IPADDRESS','LOCATION','CITY','REGION','COUNTRY','ORGANIZATION'])
        handler = ipinfo.getHandler(access_token)
        with open(self.input, 'r') as loa:
            for ip in loa:
                details = handler.getDetails(ip)
                outputWriter.writerow([details.ip,details.loc,details.city,details.region,details.country,details.org])
            print "Finished"
        
        
if __name__ == "__main__":
    banner = '''        
.__       .__        _____       
|__|_____ |__| _____/ ____\____  
|  \____ \|  |/    \   __\/  _ \ 
|  |  |_> >  |   |  \  | (  <_> )
|__|   __/|__|___|  /__|  \____/ 
   |__|           \/             
   by@tunisj
   '''
   
    parser = argparse.ArgumentParser(description='getipinfo by@tunisj')

    parser.add_argument(
        '-i', '--input',
        action='store',
        dest='input',
        help='List of IP Addresses to use',
        default='listofipaddresses.txt'
    )
    parser.add_argument(
        '-o', '--output',
        action='store',
        dest='output',
        help='Output to save valid results',
        default='output.csv'
    )
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()
    
    print (banner)
    get_ipinfo = getipinfo(
        args.input,
        args.output
    )
    get_ipinfo.main()
