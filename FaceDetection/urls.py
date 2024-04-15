

from django.urls import path 

from . import views
app_name = 'FaceDetection'

urlpatterns = [
    path("facedetection/" , views.show , name='facedetection'),
    path("FaceDetectionVedio/" , views.video_show , name='FaceDetectionVedio'),
    # Another Tab Inside Show the Video
    # path("videoshow/" , views.video_show , name = 'videoshow'),
    path("videoshow/" , views.video_show , name= "videoshow"),
    path("video_show/" , views.videoshow , name= "video_show"),






]