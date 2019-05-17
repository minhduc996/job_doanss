from django.urls import path
from job import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='homepage'),
    path('dang-du-an.html', views.dangduan, name='dang-du-an'),
    path('dang-viec-tuyen-dung.html', views.dangviectuyendung, name='dang-viec-tuyen-dung'),
    path('dang-cuoc-thi.html', views.dangcuocthi, name='dang-cuoc-thi')
]
