from django.shortcuts import render, redirect
from .models import Myinfo
from .models import Write
from .forms import WriteForm
from django.views import View
from django.utils.safestring import mark_safe
from .models import Calendar
import json
# Create your views here.

def base(request):
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
    write_diary = Write.objects.all()
    context = {'write_diary': write_diary}
    if request.method == 'POST':
        diary = Write(date=request.POST.get('date'),
                          title=request.POST.get('title'),
                          content=request.POST.get('content'))
        # diary.date = request.POST.get('date')
        # diary.title = request.POST.get('title')
        # diary.content = request.POST.get('content')
        diary.save()
        return render(request,'diary/list.html', context)

# views.py
class CalendarView(View):
    def get(self, request):
        events = Calendar.objects.all()
        event_list = []
        for event in events:
            event_list.append({
                'title': event.title,
                'start': str(event.start_time),
                'end': str(event.end_time),
            })
        event_list = mark_safe(json.dumps(event_list))

        return render(request, 'diary/calendar.html', {'events': event_list})

