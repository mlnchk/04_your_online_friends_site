import requests
import json
import sys
import time
from auth import get_access_token


def get_all(search):
    api_url = 'https://api.vk.com/method/'
    method = 'users.get'
    method2 = 'friends.getOnline'
    # print('enter url from address stroke')
    # time.sleep(3)
    # token = get_access_token()
    token = 'ba92a5ba3a4ff5ddc0db20664bf2e51b80e6e7667ac63b0652e3dc2dcb1e8a919707e0482faeb91833617'

    # if len(sys.argv) == 1:
    #     # print('enter id/domain')
    #     search = 30026908
    #     # search = input()
    # else:
    #     search = sys.argv[1]

    params = {
        'access_token': token,
        'fields': 'photo_50'
    }

    if type(search) == str:
        params['user_ids'] = search
        find = json.loads(requests.get(api_url + method, params).text)['response'][0]['uid']
        params['user_id'] = find
    else:
        params['user_id'] = search

    id_lst = json.loads(requests.get(api_url + method2, params).text)['response']
    # print('Friends online: \n')

    params['user_ids'] = ', '.join(map(str, id_lst))
    all = []
    links = []
    names2 = []
    photos = []
    names = json.loads(requests.get(api_url + method, params).text)['response']
    for name in names:
        # print('vk.com/id' + str(name['uid']), '\t', name['first_name'], name['last_name'])
        # a = 'vk.com/id%s %s %s' % (str(name['uid']), name['first_name'], name['last_name'])
        a = 'https://vk.com/id%s' % name['uid']
        b = '%s %s' % (name['first_name'], name['last_name'])
        c = name['photo_50']
        links.append(a)
        names2.append(b)
        photos.append(c)
    # all = zip(links, names)
    print(photos)
    return links, names2, photos

# l, n = get_all('lanaed')
# print(l)
# print(n)
#
# for i in zip(l, n):
#     print(i)