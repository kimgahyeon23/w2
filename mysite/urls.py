"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from mysite.views import HomeView,UserCreateView,UserCreateDoneTV
from django.conf.urls.static import static
from django.conf import settings
from bookmark.views import BookmarkLV, BookmarkDV
#from bookmark.views import index, detail
#여기에 없는 주소를 요청시 404 낫 파운드 에러가 나는거임
urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('admin/', admin.site.urls),
    path('bookmark/' ,include('bookmark.urls')),
    # /bookmark/urls안의 path들에게 내용이 전달되서 실행됌
    #include(bookmark.urls)을 함으로써 bookmark안의 urls.py안의 파일을 가져옴

    # path(a b c) a같은 요청이 오면 b로 처리하겠다
    # a/<숫자> -> 숫자 = id 보고싶은 id값을 넣는것
    # path variable이라고 부름 /<숫자> 를 경로 변수 표기는 꺽새로 함
    # <타입:pk>primary key

    #name = 주소명이 바뀔수있는데 name을 등록함으로써 바꿀일을 없게하겠다

    #path("bookmark/", index, name = "index"),
    #path("bookmark/<int:pk>",detail,name='detail'),
    path('blog/', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(),
         name='register_done'),
    path('tinymce/', include('tinymce.urls')),
    path('api/', include('api.urls')),

]


# ○ admin/
# ▪ 관리자 페이지를 django가 자동으로 생성해줌
# ○ urlpatterns
# ▪ 처리할 url의 목록을 가짐
# ○ path(<url 문자열>, <뷰 함수>, [name])