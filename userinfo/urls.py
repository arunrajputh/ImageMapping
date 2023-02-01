from django.urls import path


from . import views


urlpatterns=[
            path('', views.userregister,name='userregister'),
            path('verify/', views.verify_image,name='verify_image'),
]
