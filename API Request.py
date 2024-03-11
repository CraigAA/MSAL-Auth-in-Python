import msal
import requests
import json

config = json.load(open("C:\Users\\atking\Desktop\parameters.json"))

connect = msal.ConfidentialClientApplication(
    config["client_id"], authority=config["authority"],
    client_credential=config["secret"]
    )
result = connect.acquire_token_silent(config["scope"], account=None)

if not result:
    result = connect.acquire_token_for_client(scopes=config["scope"])

if "access_token" in result:
    print('Token Aquired')
    token='Bearer {}'.format(result['access_token'])    
# please note- use dataareaId filter and cross-company to get better results 
    queryParams = "/data/SPR_Lab?$filter=ProdId eq 'PRO000010482' and dataAreaId eq '5150' &cross-company=true"
    productionOrdersUrl = '{}{}'.format(config["ActiveDirectoryResource"],queryParams)
    data = requests.get(  # Use token to call downstream service
        url=productionOrdersUrl,headers={'Authorization': token}).json()
    print(data)

