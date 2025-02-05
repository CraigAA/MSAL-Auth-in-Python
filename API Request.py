import msal
import requests
import json

config = json.load(open("C:\parameters.json"))

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

    table_name = 'SPR_Lab'
    filter =  '?$filter= '

    # please note- use dataareaId filter and cross-company to get better results 
    queryParams = "/data/"+table_name+filter+" dataAreaId eq '5150' &cross-company=true"
    urlFormatted = '{}{}'.format(config["ActiveDirectoryResource"],queryParams)
    data = requests.get(  # Use token to call downstream service
        url=urlFormatted,headers={'Authorization': token}).json()
    
    print(data)

