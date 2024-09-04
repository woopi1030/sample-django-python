"""
URL configuration for sample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path("polls/", include("polls.urls")),
    path('admin/', admin.site.urls),
]


"""
path() 함수에는 2개의 필수 인수인 route 와 view, 2개의 선택 가능한 인수로 kwargs 와 name 까지 모두 4개의 인수가 전달 되었습니다. 이 시점에서, 이 인수들이 무엇인지 살펴보는 것은 의미가 있습니다.

path() 인수: route¶
route 는 URL 패턴을 가진 문자열 입니다.  요청이 처리될 때, Django 는 urlpatterns 의 첫 번째 패턴부터 시작하여, 일치하는 패턴을 찾을 때 까지 요청된 URL 을 각 패턴과 리스트의 순서대로 비교합니다.

패턴들은 GET 이나 POST 의 매개 변수들, 혹은 도메인 이름을 검색하지 않습니다. 예를 들어, https://www.example.com/myapp/ 이 요청된 경우, URLconf 는 오직 myapp/ 부분만 바라 봅니다. https://www.example.com/myapp/?page=3, 같은 요청에도, URLconf 는 역시 myapp/ 부분만 신경씁니다.

path() 인수: view¶
Django 에서 일치하는 패턴을 찾으면, HttpRequest 객체를 첫번째 인수로 하고, 경로로 부터 ‘캡처된’ 값을 키워드 인수로하여 특정한 view 함수를 호출합니다. 나중에 이에 대한 간단한 예제를 살펴보겠습니다.

path() 인수: kwargs¶
임의의 키워드 인수들은 목표한 view 에 사전형으로 전달됩니다. 그러나 이 튜토리얼에서는 사용하지 않을겁니다.

path() 인수: name¶
URL 에 이름을 지으면, 템플릿을 포함한 Django 어디에서나 명확하게 참조할 수 있습니다. 이 강력한 기능을 이용하여, 단 하나의 파일만 수정해도 project 내의 모든 URL 패턴을 바꿀 수 있도록 도와줍니다.

request 와 response 의 기본 흐름을 이해하셨다면, 튜토리얼 2장 에서 데이터베이스 작업을 시작해보세요.
"""