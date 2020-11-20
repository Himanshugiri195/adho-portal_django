from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('blog/', views.blog, name='blog'),
    path('checkstat/search',views.search, name='search'),
    path('newtick/',views.createtick,name='create'),
    path('checkstat/',views.checkreq,name='checkreq'),
    path('newtick/add',views.add,name='add'),
    path('add',views.add,name='add')
    
    
]