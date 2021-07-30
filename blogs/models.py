from django.db import models

CATEGORY =(( '仕事','仕事'),('トピック','トピック'),('定年','定年'),('人生','人生'),('健康','健康'),('趣味','趣味'),('家庭','家庭'))
class Blog(models.Model):
	category = models.CharField(blank=True,null=True,max_length=150,choices=CATEGORY)
	title = models.CharField(blank=False,null=False,max_length=150)
	text = models.TextField(blank=True)
	created_datetime = models.DateTimeField(auto_now_add=True)
	updated_datetime = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title
