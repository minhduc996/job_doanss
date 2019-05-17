from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def dangduan(request):
    return render(request, "dang-du-an.html", {})

def dangviectuyendung(request):
    return render(request, "dang-viec-tuyen-dung.html", {})


def dangcuocthi(request):
    return render(request, "dang-cuoc-thi.html", {})