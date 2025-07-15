from rest_framework import serializers
from .models import Student,Course,Enrollment


class StudentSerializer(serializers.ModelSerializer) :
 class Meta :
  model = Student
  fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
 class Meta:
  model = Course
  fields = '__all__'


class EnrollmetnSerializer(serializers.ModelSerializer):
 
 student = StudentSerializer(read_only=True)
 course = CourseSerializer(read_only=True)
 student_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), source='cours', write_only=True)


class Meta :
  model = Enrollment
  fields = ['id', 'student', 'course', 'date_enrolled', 'student_id' 'course_id']
  
 