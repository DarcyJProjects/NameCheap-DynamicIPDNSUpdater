#IMPORTS
import urllib.request as urllib2
from requests import get
from datetime import datetime

#-------------------------------------------------------------------------#
#NAMECHEAP INFO - ensure no spaces
hosts = ["@", "www"]
domain_name = 'YourDomainName.com.au'
dynamic_dns_password = 'YourNameCheapDynamicDNSPassword'

#FILE-PATHS
last_ip_file = r'./last.ip'
run_log_file = r'./run.log'
#-------------------------------------------------------------------------#

#VARIABLES
last_ip = ''
current_ip = ''

now = datetime.now()
now_formatted = now.strftime("%d/%m/%Y %H:%M:%S")
print("Running: ", now_formatted)	

print("Checking last known IP address...")
file1 = open(last_ip_file,"r") #read only
last_ip = file1.read()
file1.close()

print("Getting current IP address...")
current_ip = get('https://api.ipify.org').content.decode('utf8')

print("Comparing IP addresses...")
if (current_ip != last_ip):
    print("IP Addresses do not match.")
    print("Logging new IP.")
    file1 = open(last_ip_file,"w") #write over
    file1.write(current_ip)
    file1.close()

    print("Updating IP address on DNS Records for specified hosts of " + domain_name)

    for i in hosts:
        api_url = "https://dynamicdns.park-your-domain.com/update?host=" + i + "&domain=" + domain_name + "&password=" + dynamic_dns_password + "&ip=" + current_ip
        urllib2.urlopen(api_url)

    file1 = open(run_log_file,"a") #append
    file1.write("[" + now_formatted + "] - UPDATED!" + "\n")
    file1.close()    

    print("Finished. Exiting...")
    quit()
    
print("No Difference. Exiting...")
quit()
