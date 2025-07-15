from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
class Enrollment(models.Model):
    studant = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollement')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollment')
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.studant.name} - {self.course.title}"
