from django.shortcuts import render , redirect

# Create your views here.
from .models import Image
from .forms import ImageForm
from django.http import HttpResponse

import cv2
import face_recognition
import os
import numpy as np
path = "new_att"


images = []
classname = []
print(" Cal Now")
mylist = os.listdir(path)


for cls in mylist:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    # print(cls)
    name = ""
    for i in cls:
        if i == ".":
            break
        else:
            name += i
    if name not in classname:
        classname.append(name)

print(classname)


def findEncoding(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(img)
        if len(face_encodings) > 0:
            encode = face_encodings[0]
            encodelist.append(encode)
        else:
            print("No face detected in the image.")
    return encodelist

encodelistknown = findEncoding(images)
print(len(encodelistknown))





# ------------------------------------------------------------
def show(request):
    if request.method == "POST":
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('show')
        
    form = ImageForm()
    img = Image.objects.all()

    last_image = Image.objects.last()


    

    form = ImageForm()


    

    
    return render (request , "FaceDetection/FaceDetection_first.html" , {'last_image':last_image , 'form':form})
    # return render(request, 'FaceDetection/FaceDetection_first.html')

    
def video_show(request):

    return render(request , "FaceDetection/FaceDetection_second.html" )
