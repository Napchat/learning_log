"""
定义learning_logs的URL模式
"""
from django.conf.urls import url
from . import views

# 该列表表示可在应用程序learning_logs中请求的网页
urlpatterns = [
	# 主页
	url(r'^$', views.index, name='index'),     #将URL映射到视图

	# 显示所有的主题
	url(r'^topics/$', views.topics, name='topics'),

	# 特定主题的详细页面
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

	# 用于添加新主题的页面
	url(r'^new_topic/$', views.new_topic, name='new_topic'),

	# 用于添加新条目的页面
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

	# 显示所有的合作者
	url(r'^coworkers/$', views.coworkers, name='coworkers'),

	# 用于编辑条目的页面
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
