import webbrowser


def get_access_token():
    auth_url = 'https://oauth.vk.com/authorize?client_id=5899797&display=page&redirect_uri=' \
               'https://oauth.vk.com/blank.html&scope=65538&response_type=token&v=5.52'
    webbrowser.open(auth_url, new=2)
    copied_url = input("Paste here url you were redirected:\n")
    access_token = copied_url[copied_url.find('access_token') + 13:copied_url.find('&')]
    return access_token
