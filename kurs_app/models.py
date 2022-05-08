from django.contrib.auth.models import User
from django.db import models

class Teacher(models.Model):
    firsname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    rasm = models.FileField(blank=True, upload_to='Teacher')
    approved = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.firsname

class Student(models.Model):
    firsname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    rasm = models.FileField(blank=True,upload_to='Student')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.firsname

class Course(models.Model):
    Ch = (
        ('Easy', 'Easy'),
        ('Hard', 'Hard'),
        ('Medium', 'Medium')
    )
    name = models.CharField(max_length=150)
    narxi = models.IntegerField()
    rasm = models.FileField(upload_to='Course')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    daraja = models.CharField(max_length=15,choices=Ch)
    def __str__(self):
        return self.name

class Content(models.Model):
    nomi = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nomi

class Video(models.Model):
    video = models.FileField()
    duration = models.DurationField()
    data = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)
    content = models.ForeignKey(Content, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    video = models.ForeignKey(Video,  on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student,  on_delete=models.SET_NULL, null=True)
    matn = models.TextField(default="zur")
    rating = models.PositiveSmallIntegerField()

class Royxat(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student


