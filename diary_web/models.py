from django.db import models
# from schedule.models import Event as BaseEvent

# Create your models here.


class Myinfo(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    birth = models.DateTimeField('date published')
    age = models.IntegerField()

class Write(models.Model):
    date = models.DateField('Y%-m%-d%')
    title = models.CharField('',max_length=200)
    content = models.CharField('',max_length=1000)

# class Event(BaseEvent):
#     color = models.CharField(max_length=7, default='#0071c5')
class Calendar(models.Model):
    # userId = models.IntegerField(default=0) # 사용자 아이디 (Admin users 테이블의 PK)
    title = models.CharField(max_length=100) # 이벤트 제목
    start = models.DateTimeField('Start Date') # 이벤트 시작일시
    end = models.DateTimeField('End Date') # 이벤트 종료일시
    # allDay = models.BooleanField(default=True) # 이벤트가 종일 지속되는지 여부

    def __str__(self) -> str:
        return self.title