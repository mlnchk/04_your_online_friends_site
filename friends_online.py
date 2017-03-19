import requests
import json
import sys
import time
from auth import get_access_token


api_url = 'https://api.vk.com/method/'
get_users_method = 'users.get'
get_friends_online_method = 'friends.getOnline'
token = 'ba92a5ba3a4ff5ddc0db20664bf2e51b80e6e7667ac63b0652e3dc2dcb1e8a919707e0482faeb91833617'

params = {
    'access_token': token,
    'fields': 'photo_50'
}


def search_by_domain(search_query):
    params['user_ids'] = search_query
    found_user = json.loads(requests.get(api_url + get_users_method, params).text)['response'][0]['uid']
    params['user_id'] = found_user


def compile_data(persons):
    links, names, photos = [], [], []
    for person in persons:
        links.append('https://vk.com/id%s' % person['uid'])
        names.append('%s %s' % (person['first_name'], person['last_name']))
        photos.append(person['photo_50'])
    necessary_data = zip(links, names, photos)
    return necessary_data


def get_all(search_query):
    if type(search_query) == str:
        search_by_domain(search_query)
    else:
        params['user_id'] = search_query

    id_list = json.loads(requests.get(api_url + get_friends_online_method, params).text)['response']
    params['user_ids'] = ', '.join(map(str, id_list))

    persons = json.loads(requests.get(api_url + get_users_method, params).text)['response']
    return compile_data(persons)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        # print('enter id/domain')
        search_query = 30026908
        # search_query = input()
    else:
        search_query = sys.argv[1]
    print('Friends online: \n')
    for data_set in get_all(search_query):
        print(data_set[0], '\t', data_set[1])
