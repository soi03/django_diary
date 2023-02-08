"""diary URL Configuration
    url mapper file

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from diary_web import views

app_name = 'diary'

urlpatterns = [
    path('admin/', admin.site.urls),
    # 1. GET / diary/ 
    # path에 접근할 때 views파일의 base를 실행해라  
    path('', views.base, name ='base'), # 메인페이지
    # 2. GET / diary / new / 
    path('write/', views.write, name ='write'), # 일기 작성
    # # 3. POST / diary / new / 
    # # path('create/', views.create, name ='create'), # 게시글 생성! (POST)
    # # 4. GET / diary / 1/ 
    # path('<int:pk>/', views.detail, name= 'detail'),
    # # 5. POST / diary /1/ delete/ 
    # path('<int:pk>/delete/', views.delete, name='delete'),
    # # 6. GET /diary /1/edit/
    # path('<int:pk>/edit/', views.edit,name ='edit'), # 게시글 수정 양식 (GET)
    # # 7. POST / diary/1/edit/
    # # path('update/<int:pk>/', views.update, name = 'update'), # 게시글 수정! (POST)
]

# img태그 사용시 사용..? 불필요시 삭제하기
# from django.conf.urls.static import static
# from django.conf import settings
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)