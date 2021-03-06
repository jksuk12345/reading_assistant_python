# -*- coding: utf-8 -*-
'''
Created on 2013. 5. 29.


'''
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from lxml import etree, objectify
from reading_assistant.common.naver_openapi_book import NaverOpenApiBook
from reading_assistant.common.page_navigation import PageNavigation
from reading_assistant.models import Book, BookForm, UserForm, BestWord, Review, \
    ReadingNowForm, ReadingNow

def list(request):
    bookListTotalRowCnt = len(Book.objects.all())
    pageNavigation = PageNavigation(request, bookListTotalRowCnt)

    return render_to_response('book/book_list.html', {
        'book_list' : Book.objects.order_by('-reg_dt')[pageNavigation.startNo:pageNavigation.lastNo],
        'cur_page' : pageNavigation.curPage,
        'page_navigation_max_cnt' : pageNavigation.pageNavigationMaxCnt,
        'page_row_cnt' : pageNavigation.pageRowCnt,
        'page_navigation_html' : pageNavigation.pageNavigationHtml,
        'book_list_total_row_cnt' : bookListTotalRowCnt,
    }, context_instance = RequestContext(request));

def insert_form(request):
    return render_to_response('book/book_insert.html', {
    }, context_instance = RequestContext(request));
    
def insert(request):
    bookApi = NaverOpenApiBook()
    
    resBody = bookApi.searchDetailForNaver(request.POST['link']);
    
    bSoup = BeautifulSoup(resBody, "html.parser")

    bookInfoInner = bSoup.find('div', class_='book_info_inner')
    total_score = bookInfoInner.find('div', class_='txt_desc').find('strong').get_text().replace(u'점', '')
    total_page = 0
    emList = bookInfoInner.findAll('em')
    for emInfo in emList :
        if unicode(emInfo.get_text().strip()).find(u'페이지') > -1 :
            total_page = emInfo.next_sibling.strip()

    resBody = bookApi.searchDetailInfo(request.POST['query'], request.POST['isbn'].split(' ')[1])
    rss = objectify.XML(resBody)
    
    bookFormData = {
        'user_score' : total_score,
        'current_page' : 0,
        'total_page' : total_page,
        'isbn' : unicode(rss.channel.item[0].isbn).split(' ')[1],
        'book_name' : unicode(rss.channel.item[0].title),
        'author' : unicode(rss.channel.item[0].author),
        'publisher' : unicode(rss.channel.item[0].publisher),
        'pub_date' : unicode(rss.channel.item[0].pubdate),
        'image_url' : rss.channel.item[0].image,
        'link_naver' : rss.channel.item[0].link,
        'user' : request.session.get('id')
    }

    bookForm = BookForm(bookFormData)
    
    if bookForm.is_valid() :
        bookForm.save()
    else :
        print bookForm.errors
        return HttpResponse('<script>alert("폼 유효성 검사 실패!");history.back();</script>')

    return HttpResponseRedirect("/book/book_list")

def detail(request):
    isbn = request.POST['isbn']
    book = Book.objects.get(isbn=isbn)

    return render_to_response('book/book_detail.html', {
        'book' : book,
        'bestword_list' : BestWord.objects.select_related().filter(book=book).order_by('-reg_dt'),
        'review_list' : Review.objects.select_related().filter(book=book).order_by('-reg_dt'),
        'current_ratio' : float(book.current_page) / float(book.total_page) * 100.0,
    }, context_instance = RequestContext(request));

def delete(request):
    isbn = request.POST['isbn']
    book = Book(isbn=isbn)
    book.delete()
    
    return HttpResponseRedirect("/book/book_list")

def update_current_page(request):
    isbn = request.POST['isbn']
    current_page = request.POST['current_page']
     
    book = Book.objects.get(isbn=isbn)
    book.current_page = current_page
    book.save()
    
    readingNowFormData = {
        'current_page' : current_page,
        'current_ratio' : float(book.current_page) / float(book.total_page) * 100.0,
        'book' : isbn,
        'user' : request.session.get('id')
    }
    
    readingNow = ReadingNowForm(readingNowFormData)
    readingNow.save()
    
    book = Book.objects.get(isbn=isbn)
    
    return render_to_response('book/book_detail.html', {
        'book' : book,
        'bestword_list' : BestWord.objects.select_related().filter(book=book).order_by('-reg_dt'),
        'review_list' : Review.objects.select_related().filter(book=book).order_by('-reg_dt'),
        'current_ratio' : float(book.current_page) / float(book.total_page) * 100.0,
    }, context_instance = RequestContext(request));

def search_result(request):
    book_name = request.GET['book_name']
    bookApi = NaverOpenApiBook()
    
    start = 1
    
    pageRowCnt = 10
    if request.GET.has_key('curPage'):
            if int(request.GET['curPage']) > 0:
                curPage = int(request.GET['curPage'])
                start = (curPage * pageRowCnt) + 1
    
    resBody = bookApi.searchBaseInfo(book_name, start)
    rss = objectify.XML(resBody)
    
    total_row_cnt = rss.channel.total.text
    
    if total_row_cnt > 1000:
        total_row_cnt = 1000
    
    pageNavigation = PageNavigation(request, total_row_cnt)
    
    return render_to_response('book/book_search_result.html', {
        'rss' : rss,
        'cur_page' : pageNavigation.curPage,
        'page_navigation_max_cnt' : pageNavigation.pageNavigationMaxCnt,
        'page_row_cnt' : pageNavigation.pageRowCnt,
        'page_navigation_html' : pageNavigation.pageNavigationHtml,
        'book_list_total_row_cnt' : total_row_cnt,
    }, context_instance = RequestContext(request));