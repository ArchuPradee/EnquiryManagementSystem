from django.urls import path,include
from . import views

urlpatterns = [
    path('categories', views.ListCategory.as_view(), name='category'),
    path('categories/<int:pk>/', views.DetailCategory.as_view(), name='singlecategory'),
    
    path('courses', views.ListCourse.as_view(), name='courses'),
    path('courses/<int:pk>/', views.DetailCourse.as_view(), name='singlecourse'),

    path('students', views.ListStudent.as_view(), name='students'),
    path('students/<int:pk>/', views.DetailStudent.as_view(), name='singlestudent'),

    path('users', views.ListUser.as_view(), name='users'),
    path('users/<int:pk>/', views.DetailUser.as_view(), name='singleuser'),

    path('enquires', views.ListEnquiry.as_view(), name='allenquires'),
    path('enquires/<int:pk>', views.DetailEnquiry.as_view(), name='enquirydetail'),
]
