"""
定义learning_logs的URL模式
"""
from django.conf.urls import url
from . import views

# 该列表表示可在应用程序learning_logs中请求的网页
urlpatterns = [
	# 主页
	url(r'^$', views.index, name='index'),     #将URL映射到视图
]
