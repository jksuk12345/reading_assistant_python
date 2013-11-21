# -*- coding: utf-8 -*-
'''
Created on 2013. 5. 29.


'''
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from reading_assistant.models import Book, ReviewForm, Review, BestWord

def insert_form(request):
    email = request.POST['user']
    isbn = request.POST['book']
    
    book = Book(isbn=isbn)
    
    return render_to_response('review/review_insert.html', {
        'user_email' : email,
        'book_isbn' : isbn,
        'book' : book,
    }, context_instance = RequestContext(request));
    
def insert(request):
    reviewForm = ReviewForm(request.POST)
    
    if reviewForm.is_valid() :
        reviewForm.save()
    else :
        print reviewForm.errors
        return HttpResponse('<script>alert("폼 유효성 검사 실패!\n");history.back();</script>')

    isbn = request.POST['isbn']
    book = Book.objects.get(isbn=isbn)
    
    return render_to_response('book/book_detail.html', {
        'book' : book,
        'bestword_list' : BestWord.objects.select_related().filter(book=book).order_by('-reg_dt'),
        'review_list' : Review.objects.select_related().filter(book=book).order_by('-reg_dt'),
        'current_ratio' : float(book.current_page) / float(book.total_page) * 100.0,
    }, context_instance = RequestContext(request));

def delete(request):
    review_name = request.POST['review_name']
    review = Review(review_name=review_name)
    review.delete()
    
    isbn = request.POST['isbn']
    book = Book.objects.get(isbn=isbn)
    
    return render_to_response('book/book_detail.html', {
        'book' : book,
        'bestword_list' : BestWord.objects.select_related().filter(book=book).order_by('-reg_dt'),
        'review_list' : Review.objects.select_related().filter(book=book).order_by('-reg_dt'),
        'current_ratio' : float(book.current_page) / float(book.total_page) * 100.0,
    }, context_instance = RequestContext(request));