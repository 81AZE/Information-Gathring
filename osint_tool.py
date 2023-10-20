import argparse
import colorama
import dns.resolver
import requests
import shodan
import socket
import whois


colorama.init(autoreset=True)

argparse = argparse.ArgumentParser(description="This is a Open-source Automation lool..", usage=" %(prog)s -d DOMAIN ", epilog=colorama.Style.BRIGHT + "This tool is created by Krishanu aka:81az3.")
argparse.add_argument("-d","--domain",help="Enter the domain name/IP for OSINT.", required=True)
argparse.add_argument("-o","--output",help="Enter the file to write output to.")

args = argparse.parse_args()
domain = args.domain
output = args.output


# whois module

print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "[+] Getting whois info..")
whois_result = ''

# using whois library, creating instance

try:
    py = whois.query(domain)
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "[+] whois info found.")
    whois_result += "Name: {}".format(py.name) + '\n'
    whois_result += "Registrar: {}".format(py.registrar) + '\n'
    whois_result += "Creation Date: {}".format(py.creation_date) + '\n'
    whois_result += "Expiration date: {}".format(py.expiration_date) + '\n'
    whois_result += "Registrant: {}".format(py.registrant) + '\n'
    whois_result += "Registrant Country: {}".format(py.registrant_country) + '\n'

except:
    pass
print(colorama.Fore.GREEN + whois_result)


#DNS module

print(colorama.Fore.BLUE + colorama.Style.BRIGHT + "[+] Getting DNS info..")
dns_result = ''

#implementing dns.resolver from dnspython

try:
    for a in dns.resolver.resolve(domain,'A'):
        dns_result += "[+] A Record: {}".format(a.to_text()) + '\n'
    for ns in dns.resolver.resolve(domain, 'NS'):
        dns_result += "[+] NS Record: {}".format(ns.to_text())  + '\n'
    for mx in dns.resolver.resolve(domain, 'MX'):
        dns_result += "[+] MX Record: {}".format(mx.to_text()) + '\n'
    for txt in dns.resolver.resolve(domain, 'TXT'):
        dns_result += "[+] TXT Record: {}".format(txt.to_text())  + '\n'
except:
    pass
print(colorama.Fore.BLUE+dns_result)


#Geolocation module

print(colorama.Fore.BLACK + colorama.Style.BRIGHT + "[+] Getting geolocation info..")
geo_result = ''

#implementing requests for web request

try:
    response = requests.request('GET', "https://geolocation-db.com/json/" + socket.gethostbyname(domain)).json()
    geo_result += "[+] Country: {}".format(response['country_name']) + '\n'
    geo_result += "[+] Latitude: {}".format(response['latitude']) + '\n'
    geo_result += "[+] Longitude: {}".format(response['longitude']) + '\n'
    geo_result += "[+] City: {}".format(response['city']) + '\n'
    geo_result += "[+] State: {}".format(response['state']) + '\n'
except:
    pass
print(colorama.Fore.BLACK + geo_result)


#shodan module
shodan_key = "Z6gCFZcvZoFpBofmhur4CKwQTUyRpGm6"
if domain:
    print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "[+] Getting info from Shodan for IP {}".format(domain))
    #shodan API
    api = shodan.Shodan(shodan_key)
    try:
        results = api.search(domain, page=1)
        print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "[+] Results found: {}".format(results['total']))
        for result in results['matches']:
            print(colorama.Fore.YELLOW + "[+] IP: {}".format(result['ip_str']))
            print(colorama.Fore.YELLOW + "[+] Data: \n{}".format(result['data']))
            print()

    except:
        print(colorama.Fore.RED + "[-] Shodan search error.")


if (output):
    with open(output, 'w') as file:
        file.write(whois_result + '\n\n')
        file.write(dns_result + '\n\n')
        file.write(geo_result + '\n\n')
