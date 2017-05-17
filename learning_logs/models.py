from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 每一个model相当于一个数据库表
class Topic(models.Model):
	'''用户学习的主题'''
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)

	def __str__(self):
		'''返回模型的字符串表示'''
		return self.text

class Entry(models.Model):
	'''学到的有关某个主题的具体知识'''
	topic = models.ForeignKey(Topic)           #外键,Topic对象可通过属性entry_set.all()来获取该类下的属性
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		return self.text[:50] + "..."

class Coworker(models.Model):
	'''合作者'''
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text
