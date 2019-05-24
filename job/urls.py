from django.urls import path
from job import views
from job.views import ViecLamDetailView

app_name = 'job'
urlpatterns = [
    path('', views.index, name='index'),
    path('dang-du-an.html', views.Postlist.as_view(), name='list'),
    path('viec-lam-freelance.html', ViecLamDetailView.as_view(), name='lisst tesst'),
    path('index.html', views.index, name='homepage'),
    path('dang-du-an.html', views.dangduan, name='dang-du-an'),
    path('dang-viec-tuyen-dung.html', views.dangviectuyendung, name='dang-viec-tuyen-dung'),
    path('dang-cuoc-thi.html', views.dangcuocthi, name='dang-cuoc-thi'),
    path('viec-lam-freelance.html', views.vieclamfreelance, name='viec-lam'),
]

