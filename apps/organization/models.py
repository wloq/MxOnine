# _*_ encoding:utf-8 _*_
from django.db import models
from datetime import datetime

# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=20,verbose_name="城市")
    desc = models.CharField(max_length=200,verbose_name="描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50,verbose_name="机构名称")
    desc = models.TextField(verbose_name="机构描述")
    category = models.CharField(max_length=20,default="pxjg",choices=(("pxjg","培训机构"),("gr","个人"),("gx","高校")),verbose_name="机构类别")
    click_nums = models.IntegerField(default=0,verbose_name="点击数")
    fav_nums = models.IntegerField(default=0,verbose_name="收藏数")
    image = models.ImageField(upload_to="org/%Y/%m",verbose_name=u"封面图",max_length=100)
    address = models.CharField(max_length=150,verbose_name="机构地址")
    city = models.ForeignKey(CityDict,verbose_name="所在城市",on_delete=models.CASCADE)
    students = models.IntegerField(default=0,verbose_name=u"学习人数")
    course_nums = models.IntegerField(default=0,verbose_name=u"课程数")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name=u"所属机构",on_delete=models.CASCADE)
    name = models.CharField(max_length=50,verbose_name=u"教师名")
    work_year = models.IntegerField(default=0,verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50,verbose_name=u"就职公司")
    work_position = models.CharField(max_length=50,verbose_name=u"就职职位")
    points = models.CharField(max_length=50,verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

