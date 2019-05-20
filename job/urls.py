from django.urls import path
from job import views
from .models import DichVu,LinhVuc


app_name = 'job'
urlpatterns = [
    path('', views.index, name='index'),
    path('dang-du-an.html', views.Postlist.as_view(), name='list'),
    #path(r'/dang-du-an.html', views.PostNghe.as_view(), name='listw'),
    path('index.html', views.index, name='homepage'),
    path('dang-du-an.html', views.dangduan, name='dang-du-an'),
    path('dang-viec-tuyen-dung.html', views.dangviectuyendung, name='dang-viec-tuyen-dung'),
    path('dang-cuoc-thi.html', views.dangcuocthi, name='dang-cuoc-thi')
]