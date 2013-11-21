# -*- coding: utf-8 -*-
'''
Created on 2013. 5. 29.


'''
from django.http import HttpResponseRedirect, HttpResponse
from django.http.response import Http404
from django.shortcuts import render_to_response
from reading_assistant.common.page_navigation import PageNavigation
from reading_assistant.models import User, Book, BestWord, ReadingNow

def login(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    
    try :    
        user = User.objects.get(email=request.POST['id'])
        
        if user.password == request.POST['password'] :
            request.session['id'] = user.email
            request.session['password'] = user.password
            
        else :
            return HttpResponse('<script>alert("로그인 실패!");history.back();</script>')
        
    except User.DoesNotExist:
        return HttpResponse('<script>alert("존재하지 않는 사용자 입니다!");history.back();</script>')
    
    return HttpResponseRedirect("/")