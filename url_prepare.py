import requests


def geturls(urls, chapter):
    for i in range(10):
        urlmodule = 'http://www.biquge.jp/101653_42/' + str(chapter) + '.html'
        res = requests.get(urlmodule)
        if res:
            urls.append(urlmodule)
            chapter += 1
        else:
            break
    return urls
