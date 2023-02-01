#!C:\\Users\\dgooch\\AppData\\Local\\Programs\\Python\\Python311
 
import requests, json

##added these lines to prevent the warning for insecure request
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def fauth():
    ####This first section pulls the OAUTH token from fortinet
    fauth_url = "https://customerapiauth.fortinet.com/api/v1/oauth/token/"
    headers = {'Content-Type' : 'application/json; charset=utf-8'}
    body = {
        "username": "<appID>",
        "password": "<password>",
        "client_id": "flexvm",
        "grant_type": "password"
    } 


    ##This opens the api request and prints the entire thing
    try: 
        response = requests.post(
        url=fauth_url,
        headers=headers,
        json=body,
        # verify=False
        )
        jsonresponse = response.json()
    # print("Entire JSON response")
        # print(jsonresponse)

    except Exception as err:
        print(f'Other error occurred: {err}')

    ##This code assigns a variable to the access_token dictionary
    token = jsonresponse['access_token']
    return token
    # print(token)


toktype = 'Bearer '
otoken = fauth()
fin_tok = toktype+otoken


### This section will use the token to create an entitlement

flex_url = " https://support.fortinet.com/ES/api/flexvm/v1/configs/list"
headers = {'Authorization': fin_tok}
body = {
    "programSerialNumber": "<serial-number>"
} 

try: 
    response = requests.post(
    url=flex_url,
    headers=headers,
    json=body,
    # verify=False
    )
    jsonresponse = response.json()
# print("Entire JSON response")
    # print(jsonresponse)

except Exception as err:
    print(f'Other error occurred: {err}')

##This line prints the entire output of the request results in a nice readable format
print(json.dumps(jsonresponse, indent=4, sort_keys=True))

