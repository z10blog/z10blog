from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
from django.utils import timezone


class Article(models.Model):
    """文章模型"""
    STATUS_CHOICES = (
        ('p', '发布'),
        ('t', '草稿'),
        ('d', '删除'),
    )

    title = models.CharField('标题', max_length=55)
    content = models.TextField('内容')
    status = models.CharField(
        '状态', max_length=1, choices=STATUS_CHOICES, default='p')
    pub_date = models.DateTimeField('发布时间', default=timezone.now)
    changed_date = models.DateTimeField('修改时间', auto_now=True)
    views = models.PositiveIntegerField('浏览量', default=0)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', verbose_name='标签')
    category = models.ForeignKey(
        'Category', verbose_name='分类', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def viewed(self):
        """ 浏览量加1 """
        self.views += 1
        self.save(update_fields=['views'])


class Category(models.Model):
    """分类模型"""
    title = models.CharField('分类', max_length=40)
    create_time = models.DateTimeField('创建时间', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    """ 标签模型 """
    name = models.CharField('标签', max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name
