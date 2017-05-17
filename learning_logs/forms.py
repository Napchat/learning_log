from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	'''用于添加主题的表单'''
	class Meta:
		model = Topic                    #告诉Django根据哪个模型创建表单
		fields = ['text']				 #包含的字段
		labels = {'text': ''}            #生成标签
class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}
