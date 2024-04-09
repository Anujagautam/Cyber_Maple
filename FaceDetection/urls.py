

from django.urls import path 

from . import views
app_name = 'FaceDetection'

urlpatterns = [
    path("facedetection/" , views.show , name='facedetection')
]