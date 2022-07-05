from django.urls import path
from article import views

app_name = 'article'

urlpatterns = [
	#使用drf的mixin、generic视图需要用as_view配置路由
	path('',views.ArticleList.as_view(),name='list'),
	path('<int:pk>/',views.ArticleDetail.as_view(),name='detail'),
]