from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_List/', views.student_List, name='student_List'),
    path('add/', views.student_Add, name='student_Add'),
    path('edit/<int:student_id>/', views.student_Edit, name='student_Edit'),
    path('delete/<int:student_id>/', views.student_Delete, name='student_Delete')
]
