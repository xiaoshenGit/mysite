# 路由配置

from django.urls import path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.contrib import staticfiles
from . import views

app_name = 'polls'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),

    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),



    path('<int:question_id>/vote/', views.vote, name='vote')

]

# urlpatterns += staticfiles_urlpatterns()