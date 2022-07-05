"""vue_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include
from rest_framework.routers import DefaultRouter
from article import views

router = DefaultRouter()
#自动注册+id的路由
router.register(r'category', views.CategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    #使用include将在api-auth/后拼接rest_framework.urls内路由
    path('api-auth/',include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/article/',include('article.urls',namespace='article')),
]
