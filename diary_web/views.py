from django.shortcuts import render
from .models import Myinfo
# Create your views here.

def base(request):
    print(request)
    diary = Myinfo.objects.all() # 모든 데이터
    context = {'diary':diary}
    return render(request, 'diary/base.html', context)

def write(request):
    print(request)
    return render(request, 'diary/write_diary.html')

