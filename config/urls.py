

from django.contrib import admin
from django.urls import path
from schol import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('schol/list', views.student_list),
    path('schol/list/<int:pk>', views.student_list_pk),
    path('course/list', views.course_list),
]
