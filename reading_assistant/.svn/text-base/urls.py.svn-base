from django.contrib import admin
from django.conf.urls import patterns, include, url
from reading_assistant.common import view_index
from reading_assistant.common import view_login
from reading_assistant.user import view_user
from reading_assistant.book import view_book
from reading_assistant.bestword import view_best_word
from reading_assistant.review import view_review
from reading_assistant import models

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()
'''
admin.site.register(models.User)
admin.site.register(models.Book)
admin.site.register(models.BestWord)
admin.site.register(models.Review)
admin.site.register(models.ReadingNow)
'''

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reading_assistant.views.home', name='home'),
    # url(r'^reading_assistant/', include('reading_assistant.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    ('^$', view_index.index),
    ('^login/$', view_login.login),
    ('^user/user_list/$', view_user.list),
    ('^user/user_insert_form/$', view_user.insert_form),
    ('^user/user_insert/$', view_user.insert),
    ('^user/user_update_form/$', view_user.update_form),
    ('^user/user_update/$', view_user.update),
    ('^user/user_delete/$', view_user.delete),
    ('^book/book_list/$', view_book.list),
    ('^book/book_insert_form/$', view_book.insert_form),
    ('^book/book_insert/$', view_book.insert),
    ('^book/book_search_result/$', view_book.search_result),
    ('^book/book_detail/$', view_book.detail),
    ('^book/book_delete/$', view_book.delete),
    ('^book/book_current_page_update/$', view_book.update_current_page),
    ('^bestword/bestword_insert_form/$', view_best_word.insert_form),
    ('^bestword/bestword_insert/$', view_best_word.insert),
    ('^bestword/bestword_delete/$', view_best_word.delete),
    ('^review/review_insert_form/$', view_review.insert_form),
    ('^review/review_insert/$', view_review.insert),
    ('^review/review_delete/$', view_review.delete),
)
