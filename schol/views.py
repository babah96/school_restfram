from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student,Course,Enrollment
from .serializers import StudentSerializer,CourseSerializer,EnrollmetnSerializer

@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET' :
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST' :
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def student_list_pk(request, pk):
    try :
        student = Student.objects.get(pk=pk)


        if request.method == 'GET' :
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE' :
            student.delete()
            return Response(status= status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET', 'POST'])
def course_list(request):
    if request.method == 'GET':
            course = Course.objects.all()
            serialize = CourseSerializer(course, many=True)
            return Response(serialize.data)
    
    elif request.method == 'POST' :
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def course_list_pk(request, pk):
    try :
        course = Course.objects.get(pk=pk)


        if request.method == 'GET' :
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = CourseSerializer(course, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE' :
            course.delete()
            return Response(status= status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET', 'POST'])
def enrolemwnt_list(request):
    if request.method == 'GET':
        enrolement = Enrollment.objects.all()
        serialize = EnrollmetnSerializer(enrolement, many=True)
        return Response(serialize.data)
    
    elif request.method == 'POST' :
        serializer = EnrollmetnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def enrolenwnt_list_pk(request, pk):
    try :
        enrol = Enrollment.objects.get(pk=pk)


        if request.method == 'GET' :
            serializer = EnrollmetnSerializer(enrol)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = EnrollmetnSerializer(enrol, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE' :
            enrol.delete()
            return Response(status= status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    

    
    
    
    
    
    
    
    
    
    
   


