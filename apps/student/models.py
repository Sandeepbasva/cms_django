from django.db import models

# Create your models here.


year_list = ((1, 1), (2, 2), (3, 3), (4, 4))
course_list = (('B.Tech', 'B.tech'), )
gender_list = (('M', 'Male'), ('F', 'Female'), ('T', 'Transgenders'))


class Student(models.Model):
    name = models.CharField(max_length=100)
    sid = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)
    course = models.CharField(max_length=20, choices=course_list, default='B.Tech')
    year = models.IntegerField(choices=year_list, null=True)
    address = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=32)

    def __str__(self):
        return self.sid
