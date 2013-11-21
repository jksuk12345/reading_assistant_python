# -*- coding: utf-8 -*-
'''
Created on 2013. 6. 3.


'''
from lxml import etree
from lxml import objectify
import urllib, urllib2

class NaverOpenApiBook(object):
    def __init__(self):
        self.naverApiUrl = 'http://openapi.naver.com/search'
        // Your Naver Open Api Key insert here
        //self.naverApiKey = ''
        
    '''
    [응답 필드]
    rss    -    디버그를 쉽게 하고 RSS 리더기만으로 이용할 수 있게 하기 위해 만든 RSS 포맷의 컨테이너이며 그 외의 특별한 의미는 없습니다.
    channel    -    검색 결과를 포함하는 컨테이너입니다. 이 안에 있는 title, link, description 등의 항목은 참고용으로 무시해도 무방합니다.
    lastBuildDate    datetime    검색 결과를 생성한 시간입니다.
    total    integer    검색 결과 문서의 총 개수를 의미합니다.
    start    integer    검색 결과 문서 중, 문서의 시작점을 의미합니다.
    display    integer    검색된 검색 결과의 개수입니다.
    item    -    개별 검색 결과이며, title, link, description을 포함합니다.
    title    string    검색 결과 문서의 제목을 나타냅니다. 제목에서 검색어와 일치하는 부분은 <b> 태그로 감싸져 있습니다.
    link    string    검색 결과 문서의 하이퍼텍스트 link를 나타냅니다.
    image    string    썸네일 이미지의 URL입니다. 이미지가 있는 경우만 나타납니다.
    author    string    저자정보입니다.
    price    integer    정가 정보입니다. 절판도서 등으로 가격이 없으면 나타나지 않습니다.
    discount    integer    할인 가격정보입니다. 절판도서 등으로 가격이 없으면 나타나지 않습니다.
    publisher    string    출판사 정보입니다.
    pubdate    date    출간일 정보입니다.
    isbn    integer    ISBN 넘버입니다.
    description    string    검색 결과 문서의 내용을 요약한 패시지 정보입니다. 문서 전체의 내용은 link 를 따라가면, 읽을 수 있습니다. 패시지에서 검색어와 일치하는 부분은 <b> 태그로 감싸져 있습니다.
    '''

    '''
    [요청 파라메터]
    key    string (필수)    이용 등록을 통해 받은 key 스트링을 입력합니다.
    target    string (필수) : book    서비스를 위해서는 무조건 지정해야 합니다.
    query    string (필수)    검색을 원하는 질의, UTF-8 인코딩 입니다.
    display    integer : 기본값 10, 최대 100    검색결과 출력건수를 지정합니다. 최대 100 까지 가능합니다.
    start    integer : 기본값 1, 최대 1000    검색의 시작위치를 지정할 수 있습니다. 최대 1000 까지 가능합니다.
    '''        
    def searchBaseInfo(self, query, start=1):
        query = query.encode('utf-8').strip()
        print query
        values = {
            'key' : self.naverApiKey,
            'target' : 'book',
            'start' : start,
            'query' : query
        }
        request = urllib2.Request(self.naverApiUrl, urllib.urlencode(values))
        response = urllib2.urlopen(request)
        resBody = response.read()
        return resBody 
    
    '''
    [요청 파라메터]
      상세 검색은 책 제목(d_titl), 저자명(d_auth), 목차(d_cont), ISBN(d_isbn), 출판사(d_publ) 5개 항목 중에서 1개 이상 값을 입력해야 합니다.
      
    target    string (필수) : book_adv    상세검색을 위해서는 무조건 지정해야 합니다.
    query    string (필수)    검색을 원하는 질의, UTF-8 인코딩 입니다.
    d_titl    string    책 제목에서의 검색을 의미합니다.
    d_auth    string    저자명에서의 검색을 의미합니다.
    d_cont    string    목차에서의 검색을 의미합니다.
    d_isbn    string    isbn에서의 검색을 의미합니다.
    d_publ    string    출판사에서의 검색을 의미합니다.
    d_dafr    integer (ex.20000203)    검색을 원하는 책의 출간 범위를 지정합니다. (시작일)
    d_dato    integer (ex.20000203)    검색을 원하는 책의 출간 범위를 지정합니다. (종료일)
    d_catg    integer    검색을 원하는 카테고리를 지정합니다.  
    display    integer : 기본값 10, 최대 100    검색결과 출력건수를 지정합니다. 최대 100 까지 가능합니다.
    start    integer : 기본값 1, 최대 1000    검색의 시작위치를 지정할 수 있습니다. 최대 1000 까지 가능합니다.
    '''
    def searchDetailInfo(self, query, isbn):
        query = query.encode('utf-8').strip()
        values = {
            'key' : self.naverApiKey,
            'query' : query,
            'd_isbn' : isbn,
            'target' : 'book_adv'
        }
        request = urllib2.Request(self.naverApiUrl, urllib.urlencode(values))
        response = urllib2.urlopen(request)
        resBody = response.read()
        return resBody
    
    def searchDetailForNaver(self, naverBookDetailUrl):
        request = urllib2.Request(naverBookDetailUrl)
        response = urllib2.urlopen(request)
        resBody = response.read()
        return resBody
'''
query = '꾸뻬씨의 행복 여행'
isbn = '9788970637716'

bookApi = NaverOpenApiBook()
resBody = bookApi.searchBaseInfo(query)
root = etree.fromstring(resBody)
print etree.tostring(root, pretty_print=True)
print '\r\n'
print '\r\n'
print '\r\n'

resBody = bookApi.searchDetailInfo(query, isbn)
rss = objectify.XML(resBody)

root = etree.fromstring(resBody)
print etree.tostring(root, pretty_print=True)

objectifyXml = objectify.XML(test_xml)
print objectifyXml.document.get('date')
print len(objectifyXml.document.formats.format)
'''

from bs4 import BeautifulSoup

naverBookDetailUrl = 'http://book.naver.com/bookdb/book_detail.nhn?bid=124124';
request = urllib2.Request(naverBookDetailUrl)
response = urllib2.urlopen(request)
resBody = response.read()

bSoup = BeautifulSoup(resBody, "html.parser")

bookInfoInner = bSoup.find('div', class_='book_info_inner')
total_score = bookInfoInner.find('div', class_='txt_desc').find('strong').get_text()
emList = bookInfoInner.findAll('em')
for emInfo in emList :
    if emInfo.get_text().strip() == '페이지' :
        total_page = emInfo.next_sibling.strip()
