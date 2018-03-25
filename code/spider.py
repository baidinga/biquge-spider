# -*- coding:UTF-8 -*-



import requests
from bs4 import BeautifulSoup
import time



def getsoup(s, url):
    '''
    get the html soup
     '''
    html = s.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    return soup


def geturls(s, url, urls, chapternames):
    '''
    get all the urls of the specified noval
    '''
    try:
        soup = getsoup(s, url)
    except requests.exceptions.ConnectionError:
        print "出现异常:requests.exceptions.ConnectionError"
    else:
        urls_tail = soup.find_all('dd')
        for tail in urls_tail:
            k = tail.find('a')
            chaptername = k.getText()
            chapternames.append(chaptername)
            urls.append(url + k.get("href"))
        return urls, chapternames


def get_noval_text(urls, chapternames, bookname):
    with open("/Users/zhang/PycharmProjects/noval spider/" + bookname + ".txt", "w") as f:
        chaptername_index = 0
        for url in urls:
            try:
                soup = getsoup(url)
            except requests.exceptions.ConnectionError:
                print "出现异常:requests.exceptions.ConnectionError"
            else:
                text = soup.find('div', attrs={'id':"content"})
                f.write(chapternames[chaptername_index].encode('utf8') + '\n\n')
                chaptername_index += 1
                print chapternames[chaptername_index - 1].encode('utf-8')
                f.write(text.getText().encode('utf8') + '\n\n\n\n\n\n')


if __name__ == '__main__':
    urls = []
    url = input('请输入该书的url:')
    bookname = input('请输入该书的名字:')
    s = requests.session()
    chapternames = []
    print "------------正在获取url--------------"
    urls, chapternames = geturls(s, url, urls, chapternames)
    print "------------获取url成功--------------"
    print "总数量为:%d" % len(urls)
    print "------------开始爬取文章--------------"
    get_noval_text(urls, chapternames, bookname)
    print "------------成功爬取文章--------------"
