from django.shortcuts import render, redirect
from .models import Myinfo
from .forms import WriteForm
from django.utils import timezone
import logging
# Create your views here.

def base(request):
    print(request)
    diary = Myinfo.objects.all() # 모든 데이터
    context = {'diary':diary}
    return render(request, 'diary/base.html', context)

# def write(request):
#     print(request)
#     return render(request, 'diary/write_diary.html')

def write(request):
    form = WriteForm()
    return render(request, "diary/write_diary.html", {"form" : form})

def create(request):
    if request.method == 'POST':
        diary = WriteForm()
        diary.date = request.POST['date']
        diary.title = request.POST['title']
        diary.content = request.POST['content']
        diary.save()
        return redirect('/base/')
