import datetime

from django.db import models
from django.utils import timezone

#每一个class是一个模型。每一个模型是django.db.models.Model的子类。每个变量是一个字段，每个字段是Field类的实例
#每一个Field有一个可选参数，使得是人类可读的（类似说明性质的东西），放在第一个参数
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')#'date published'是说明
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#定义外键
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) #default是默认值
    def __str__(self):
        return self.choice_text