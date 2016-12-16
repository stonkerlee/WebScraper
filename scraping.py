from __future__ import print_function
from bs4 import BeautifulSoup
import urllib2
import re

def getMovieByPage(startIndex):
    URL = 'https://movie.douban.com/top250?start={0}'.format(startIndex)
    html = urllib2.urlopen(URL)
    bsObj = BeautifulSoup(html.read(), 'html.parser')
    movies = []
    for link in bsObj.findAll('a', href=re.compile('(subject)')):
        if 'href' in link.attrs:
            l = link.attrs['href']
            if l not in movies:
                movies.append(l)
    return movies


def getMoviesOfTop250():
    top250Movies = []
    startIndex = 0
    while startIndex < 250:
        top250Movies.extend(getMovieByPage(startIndex))
        startIndex += 25
    return top250Movies


def printMovieInfo(url):
    print(url, end='')
    try:
        html = urllib2.urlopen(url)
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.find('title').get_text().strip()
        print('\t' + title)
    except:
        print('\tPage not found')


if __name__ == '__main__':
    top250Movies = getMoviesOfTop250()
    for m in top250Movies:
        printMovieInfo(m)
