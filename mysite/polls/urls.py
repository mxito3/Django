from django.urls import path

from . import views

'''
Django接收到请求的时候先匹配应用名称，然后将应用名称后的其余内容传给应用的urls.py处理。
然后调用具体的函数，将request对象和分割后的url内容传给具体的视图函数处理
'''
app_name='polls'  #设置命名空间
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail,name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]