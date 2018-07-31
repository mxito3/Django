from django.conf.urls import *
from . import view,testdb
from . import search
from . import searchInPost
urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search_form$',search.search_form),
    url(r'^search$',search.search),
    url(r'^search_in_post$',searchInPost.search)
]