import datetime
import uuid
import os
from django.db import models
from django.utils import timezone
from django.db.models.fields import Field
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # was_published_recently的样式
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # ForeignKey定义了外键
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


# on_delete设置为一个传递给SET()的值或者一个回调函数的返回值
class MyModel(models.Model):
    uesr = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )

class Artist(models.Model):
    name = models.CharField(max_length=10)

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)


# 第一个元素表示存在数据库内真实的值，第二个表示页面上显示的具体内容
class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR ='SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophmore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices = YEAR_IN_SCHOOL_CHOICES,
        default = FRESHMAN,
    )


def is_upperclass(self):
    return self.year_in_school in (self.JUNIOR, self.SENIOR)


class Person(models.Model):
    friends = models.ManyToManyField("self")
    name = models.CharField(max_length=50)
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',       ## 自定义中间表
        through_fields=('group', 'person'),
    )

class Membership(models.Model):  # 这就是具体的中间表模型
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)

# test  FileField
# class TestOther(models.Model):
#     # upload = models.FileField(upload_to='uploads/')
#     upload = models.FileField(upload_to= 'uploads/%Y/%m/%d')

def directory_path(instance, filename):
    # 文件上传到MEDIA_ROOT/user_<id>/<filename>目录中
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class TestModel(models.Model):
    upload = models.FileField(upload_to=directory_path)


# test ImageField
class TestImageField(models.Model):
    upload = model.ImageFiel(upload_to=None, height_field=None, width_field=None, max_length=100,**options)

# 生成uuid
class MyUUID(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

# 保存文件路径
def images_path():
    return os.path.join(settings.LOCAL_FIlE_DIR,'images')

class MyImage(models.Model):
    file = models.FilePathField(path=images_path)

