from django.shortcuts import render
from .models import DichVu, LinhVuc, ThanhPho
from django.views.generic import ListView , DetailView , CreateView ,UpdateView ,DeleteView
from django.utils import timezone
from django.views.generic.detail import DetailView


# Create your views here.
def index(request):
    return render(request, "index.html", {})


def dangduan(request):
    return render(request, "dang-du-an.html", {})


def dangviectuyendung(request):
    return render(request, "dang-viec-tuyen-dung.html", {})


def dangcuocthi(request):
    return render(request, "dang-cuoc-thi.html", {})


# Danh sach List
class Postlist(ListView):
    template_name = 'dang-du-an.html'
    model = DichVu
    context_object_name = 'post'
    queryset = DichVu.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Postlist,self).get_context_data(**kwargs)
        context['thanhphos'] = ThanhPho.objects.all()
        context['post1'] = LinhVuc.objects.all()
        return context

