






def getFacebookVideoposter(url):
    urlsplit=url.split('/')

    # print(urlsplit)

    if urlsplit[0]=='https:':
        urlsplit=urlsplit[1:]

    # print(urlsplit)

    if urlsplit[0]=='http:':
        urlsplit=urlsplit[1:]

    # print(urlsplit)

    if urlsplit[0]=='':
        urlsplit=urlsplit[1:]

    # print(urlsplit)

    if urlsplit[0]=='www.facebook.com':
        urlsplit=urlsplit[1:]

    # print(urlsplit)

    if urlsplit[0]=='facebook.com':
        urlsplit=urlsplit[1:]

    # print(urlsplit)

    FacebookVideoPoster= urlsplit[0]

    return FacebookVideoPoster




# url = 'https://www.facebook.com/olhardigital/videos/2847883375500570/'




# FacebookVideoPoster = getFacebookVideoposter(url)

# print(FacebookVideoPoster)