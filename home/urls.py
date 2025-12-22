from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_list/', views.student_List, name='student_list'),
    path('add/', views.student_Add, name='student_add'),
    path('delete/', views.student_delete, name='student_delete')
]
