from django.conf.urls                                 import include, url
from django.contrib                                   import admin

from .                                                import views

urlpatterns = [

    url(r'^$',                          'mysite.views.home_page',                   name ='home_page'),
    url(r'^accounts/login/$',           'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$',          'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^admin/',                     include(admin.site.urls)),
    url(r'^bookmarks/$',                views.bookmarks_list,                       name='bookmarks'),
    url(r'^local/$',                    views.local,                                name='local'),
    url(r'^registrations/$',            views.registrations,                        name='registrations'),
    url(r'',                            include('diaryandcontacts.urls')),
    #url(r'',                            include('bookmarks.urls')),
]

