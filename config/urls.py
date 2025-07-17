

from django.contrib import admin
from django.urls import path
from schol import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('schol/list', views.student_list),
    path('schol/list/<int:pk>', views.student_list_pk),
    path('course/list', views.course_list),
    path('course/list/<int:pk>', views.course_list_pk),
    path('enrolement/list', views.enrolemwnt_list),
    path('enrolement/list/<int:pk>', views.enrolenwnt_list_pk),
]
