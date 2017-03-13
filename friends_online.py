import requests
import json
import time
from auth import get_access_token

api_url = 'https://api.vk.com/method/'
method = 'users.get'
method2 = 'friends.getOnline'
print('enter url from stroke')
# token = get_access_token()
token = 'f979098f3038b62932ce627dce17417204e39bf50890ae7a4c8eef6f83327dca3c49c26ea0b3182a9fa5e'
print('enter your id/domain')
# search = input()
search = 30026908

params = {
    'access_token': token,
    'user_ids': search
}

find = json.loads(requests.get(api_url + method, params).text)['response'][0]['uid']

params['user_id'] = find
id_lst = json.loads(requests.get(api_url + method2, params).text)['response']
print('Friends online: \n')
# for ids in id_lst:
#     print('vk.com/id' + str(ids))
params['user_ids'] = str(id_lst)[1:-1]
names = json.loads(requests.get(api_url + method, params).text)['response']
for name in names:
    print('vk.com/id' + str(name['uid']), '\t', name['first_name'], name['last_name'])
