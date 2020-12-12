from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'tb_groups'


class WebDb(models.Model):
    """用户模型类"""
    # verbose_name：对字段的解析说明，相当于注释的作用
    # max_length：指定字符串内容的最大长度为多少个字符
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='密码')
    # default：设置向数据库添加数据时，字段使用的默认值
    gender = models.BooleanField(default=False, verbose_name='性别')
    age = models.IntegerField(default=18, verbose_name='年龄')
    # null=True：生成数据表时，数据表的对应字段允许为NULL
    mobile = models.CharField(max_length=11, null=True, verbose_name='手机号')

    group = models.ForeignKey(Group, on_delete=models.SET_NULL,
                              null=True)

    class Meta:
        db_table = 'tb_users'