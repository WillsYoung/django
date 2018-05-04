from django.db import models

# Create your models here.


class Student(models.Model):

    s_name = models.CharField(max_length=10)
    s_tel = models.CharField(max_length=11)

    class Meta:
        db_table = 'day51_stu'


class StudentInfo(models.Model):

    i_addr = models.CharField(max_length=20)
    i_image = models.ImageField(upload_to='upload', null=True)
    s = models.OneToOneField(Student)

    class Meta:
        db_table = 'day51_stu_info'


class Visit(models.Model):
    v_url = models.CharField(max_length=30)
    v_times = models.IntegerField()

    class Meta:
        db_table = 'visit'