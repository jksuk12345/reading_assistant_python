# -*- coding: utf-8 -*-
'''
Created on 2013. 5. 29.


'''
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from reading_assistant.common.page_navigation import PageNavigation
from reading_assistant.models import User, Book, BestWord, ReadingNow

def index(request):
    if(request.session.get('id')) :
        user = User.objects.get(email=request.session.get('id'))

        return render_to_response('common/main.html', {
            'book_list' : Book.objects.select_related().filter(user=user).order_by('-reg_dt'),   
            'bestword_list' : BestWord.objects.all().filter(user=user).order_by('-reg_dt')[:10],
            'reading_now_list' : ReadingNow.objects.select_related().filter(user=user).order_by('-reg_dt')[:10],
        }, context_instance = RequestContext(request));
        
    else :
        return render_to_response('common/main.html', {
        }, context_instance = RequestContext(request));
        