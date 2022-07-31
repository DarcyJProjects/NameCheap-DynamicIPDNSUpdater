# Namecheap Dynamic IP DNS Updater

This tool will automatically update the DNS records for the specified hosts with the latest IP address of the host machine when the IP address changes (when the host machine has a dynamic IP rather than static).<br>

You will need to use separate scheduling software to automate the script (e.g. cron is what I use (on linux)).<br>
The script is written in Python, so you'll have to have that installed: [Download Python](https://www.python.org/downloads/)

Note: The Dynamic DNS feature is available only for domains pointed to Namcheaps BasicDNS, PremiumDNS or FreeDNS.

The API used to get the machines current IP:
[ttps://ip-api.com](https://api.ipify.org) (3rd party API - I have no affiliation with the creators)

## Sections
* [Installation](#installation)
* - [Download](#download)
* [Namecheap](#namecheap)
* - [Namecheap API](#namecheap-api)
* [Configuration](#configuration)
* - [Script Configuration](#script-configuration)

## Installation
#### **Download**
1. Download the files from the [github repository](https://github.com/DarcyJProjects/NameCheap-DynamicIPDNSUpdater/archive/refs/heads/main.zip)
2. Extract the zipped folder that was downloaded and move the "script.py", "last.ip" & "run.log" files to a directory of your choice.
3. Ensure the script.py file has permissions to read and write to the "last.ip" & "run.log" files.
4. Move onto getting your [Namecheap API key](#namecheap--api)

## Namecheap
#### **Namecheap API**
1. Login to your namecheap dashboard.
2. Go to Account -> Dashboard -> find your domain name -> Manage
3. Scroll down to Nameservers and ensure your domain is using the Namecheap BasicDNS, PremiumDNS or FreeDNS. If not, it will need to be set to one of these to enable the dynamic DNS feature.
4. Click on the Advanced DNS tab and scroll down to Dynamic DNS.
5. Change the status to ON/Enabled.
6. Copy the Dynamic DNS Password and note it down.
7. Move onto [Script Configuration](#script--configuration)

## Configuration
#### **Script Configuration**
1. Open the "script.py" file you downloaded and moved to your chosen directory in a suitable editing program of your choice.
2. Under "#NAMECHEAP INFO - ensure no spaces" add your hosts in the array. Each host should be contained with double quotation marks and separated with a comma (but not after the last host). For Example: hosts = ["@", "www", "subdomain1", "subdomain2"]
3. Set the "domain_name = 'enterhere.com.au'" variable to the domain name you have registered in namecheap (without any subdomain/host - i.e. not "www.yourdomain.com.au", only "yourdomain.com.au"). Ensure no spaces.
4. Set the "dynamic_dns_password = 'enterhere'" variable to the dymanic DNS password you copied off of the namecheap dashboard earlier.
5. Save and close the "script.py" file.
6. Finally, use a third party piece of software to schedule the script to run every so often. For example, you could you cron on linux to schedule it. (look up cron linux)
