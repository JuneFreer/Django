# coding=UTF-8
from django.db import models #自django.db引入models模块

# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回Topic模型的字符串表示"""
        return self.text

class Entry(models.Model): #Entry也继承了models模块中的父类Model，说明Entry和Topic都是一种Model
    """某个topic下的具体内容"""
    topic = models.ForeignKey(Topic) #topic是一个外键实例
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True) #时间戳,能够按创建顺序呈现条目

    class Meta: #嵌套Meta类
        verbose_name_plural = 'entries' #让Django用entries来表示多个条目

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + '...'
