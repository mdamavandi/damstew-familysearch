import json
import requests

# items for use in Read Current User from User API
integration_url = 'https://integration.familysearch.org'
read_current_user_url = '/platform/users/current/'
rcuxml = integration_url + read_current_user_url + '.xml'  # for xml
rcujson = integration_url + read_current_user_url + '.json'  # for json


# set up the content for the POST to retrieve token
base_url = 'https://identint.familysearch.org'  # base URL
ident_url = '/cis-web/oauth2/v3/token'  # token portion of URL

username = raw_input('Username: ')
password = raw_input('Password: ')
appkey = raw_input('App Key: ')

# payload contains the info required for password flow token getting
payload = {'username': username,  # integration account username
          'password': password,  # integration account password
          'client_id': appkey,  # app key
          'grant_type': 'password'  # grant flow type
         }

# send the post request and get the response from the server
response = requests.post(base_url+ident_url, data=payload)

# process the json response, which we may be able to do with r.json()
data = json.loads(response.text)
data2 = response.json()

# print(response)
# print(data)
# print(data2)

# use the token to request some information from the integration system
a_token = str(data['access_token'])  # use str() to turn from unicode to string
parameters = {'Authorization': 'Bearer',
              'access_token': a_token,
              'Accept': 'application/x-fs-v1+json'
             }

cureqjson = requests.get(rcujson, params=parameters)  # json request
cureqxml = requests.get(rcuxml, params=parameters)  # xml request

# print results for json
#~ print(cureqjson.content)
# print results for xml
#~ print(cureqxml.content)
currentuserdict = json.loads(cureqjson.content)  # parse json to dict
userdisplayname = str(currentuserdict['users'][0]['displayName'])  # str() used to convert out of unicode

print('Your display name is %s.' % userdisplayname)

