from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager


class Category(models.Model):
    """Defines the category to which the course belongs to"""
    Type_Choices = [
        ("Backend","Backend"),
        ("Frontend","Frontend"),
        ("Others","Others")
    ]

    title = models.CharField(max_length=255)
    type = models.CharField(max_length=10,choices=Type_Choices, default="Others")

    def __str__(self) -> str:
        return '{} {}'.format(self.title, self.type)

    class Meta:
        verbose_name_plural = "Categories"


class Course(models.Model):
    """Courses available in the institute"""
    course_name = models.CharField(max_length=255)
    course_duration = models.IntegerField()
    course_fee = models.DecimalField(max_digits=6, decimal_places=2)
    course_category = models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{} {}'.format(self.course_name,str(self.course_category).replace(" ","_"))


class CustomUser(AbstractUser):
    USER_TYPE = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    GENDER = [("M", "Male"), ("F", "Female")]
    
    email = models.EmailField(unique=True)
    user_type = models.CharField(default=1, choices=USER_TYPE, max_length=1)
    gender = models.CharField(max_length=1, choices=GENDER)

    def __str__(self):
        return self.last_name + ", " + self.first_name

class Student(models.Model):
    """Student class which has attributes for students"""
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True)
    courses = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)


    def __str__(self) -> str:
        return '{} {}'.format(self.user.first_name, self.user.last_name)

class Enquiry(models.Model):
    """Stores the details of enquiry system"""
    id = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    student = models.ForeignKey('Student',on_delete=models.CASCADE)
    course = models.ForeignKey('Course',on_delete=models.CASCADE)
    enquired_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '{} {} {}'.format(self.student_name, self.course_name, self.enquired_at)

    class Meta:
        verbose_name_plural = "Enquiries"