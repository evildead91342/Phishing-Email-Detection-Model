import requests
import time
import json
import pandas


# file_path = str(input('please Enter The File Path: '))
# domain_CSV = pandas.read_csv((file_path))

Urls = ['www.geeksforgeeks.com', 'www.google.com',
        'www.instagram.com', 'www.facebook.com', 'klai.org.in']

API_key = '09cb4f8901fdaf4d859dc96a87d596ea1ae419ae1ed2219bb25baf056d5adbb7'
url = 'https://www.virustotal.com/vtapi/v2/url/report'
headers = {
    "accept": "application/json",
    "x-apikey": "09cb4f8901fdaf4d859dc96a87d596ea1ae419ae1ed2219bb25baf056d5adbb7",
    "content-type": "application/json"
}

parameters = {'apikey': API_key, 'resource': Urls}

for i in Urls:
    parameters = {'apikey': API_key, 'resource': i}

    response = requests.get(url=url, params=parameters, headers=headers)
    print(response)
    json_response = json.loads(response.text)
    print(json_response)
    if json_response['response_code'] <= 0:
        with open('not Found result.txt', 'a') as notfound:
            notfound.write(i) and notfound.write(
                "\tNOT found please Scan it manually\n")
    elif json_response['response_code'] >= 1:

        if json_response['positives'] <= 1:
            with open('Virustotal Clean result.txt', 'a') as clean:
                clean.write(i) and clean.write("\t NOT malicious \n")
        else:
            with open('Virustotal Malicious result.txt', 'a') as malicious:
                malicious.write(i) and malicious.write("\t Malicious") and malicious.write(
                    "\t this Domains Detectd by   " + str(json_response['positives']) + "  Solutions\n")

    time.sleep(1)
