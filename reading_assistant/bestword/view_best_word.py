# -*- coding: utf-8 -*-
'''
Created on 2013. 5. 29.


'''
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from reading_assistant.models import Book, BestWordForm, BestWord, Review

def insert_form(request):
    email = request.POST['user']
    isbn = request.POST['book']
    
    return render_to_response('bestword/best_word_insert.html', {
        'user_email' : email,
        'book_isbn' : isbn,
    }, context_instance = RequestContext(request));
    
def insert(request):
    bestWordForm = BestWordForm(request.POST)
    
    if bestWordForm.is_valid() :
        bestWordForm.save()
    else :
        print bestWordForm.errors
        return HttpResponse('<script>alert("폼 유효성 검사 실패!");history.back();</script>')

    isbn = request.POST['isbn']
    book = Book.objects.get(isbn=isbn)
    
    return render_to_response('book/book_detail.html', {
        'book' : book,
        'bestword_list' : BestWord.objects.select_related().filter(book=book).order_by('-reg_dt'),
        'review_list' : Review.objects.select_related().filter(book=book).order_by('-reg_dt'),
        'current_ratio' : float(book.current_page) / float(book.total_page) * 100.0,
    }, context_instance = RequestContext(request));

def delete(request):
    bestwordKey = request.POST['best_word']
    bestword = BestWord(best_word=bestwordKey)
    bestword.delete()
    
    isbn = request.POST['isbn']
    book = Book.objects.get(isbn=isbn)
    
    return render_to_response('book/book_detail.html', {
        'book' : book,
        'bestword_list' : BestWord.objects.select_related().filter(book=book).order_by('-reg_dt'),
        'review_list' : Review.objects.select_related().filter(book=book).order_by('-reg_dt'),
        'current_ratio' : float(book.current_page) / float(book.total_page) * 100.0,
    }, context_instance = RequestContext(request));