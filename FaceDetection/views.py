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
    if request.method == "POST":

        cap = cv2.VideoCapture(0)

        # Check if the webcam is opened successfully
        if not cap.isOpened():
            return HttpResponse("Error: Unable to open webcam")

        # Loop to capture frames from the webcam
        while True:
            # Read frame from the webcam
            success  , img = cap.read()
            
            # Check if the frame is read successfully
            if not success:
                return HttpResponse("Error: Unable to read frame from webcam")
            imgs = cv2.resize(img , (0 , 0 ) , None , 0.25 ,0.25)
            imgs = cv2.cvtColor(imgs , cv2.COLOR_RGB2BGR)

            # Model Work Flow

            facescurframe = face_recognition.face_locations(imgs)
            encodescurframe = face_recognition.face_encodings(imgs , facescurframe)


            for encodeface , faceloc in zip(encodescurframe , facescurframe):
                matches = face_recognition.compare_faces(encodelistknown , encodeface)

                facedis = face_recognition.face_distance(encodelistknown , encodeface)

                print(facedis)

                matchindex = np.argmin(facedis)

                if matches[matchindex]:
                    name = classname[matchindex].upper()
                    print(name)

                    y1 , x2 , y2 , x1 = faceloc
                    y1 , x2 , y2 , x1  = y1*4 , x2*4 , y2*4 , x1*4 
                    cv2.rectangle(img , (x1 , y1) , (x2 , y2) , (0,255,0),2)
                    cv2.rectangle(img , (x1 , y2-35) , (x2 , y2) , (0,255,0),cv2.FILLED)
                    cv2.putText(img  ,name, (x1+6 , y2-6) , cv2.FONT_HERSHEY_COMPLEX, 1 , (255  , 255, 255,) ,2)



            # Display the frame
            cv2.imshow("WebCam Image", img)

            # Wait for a key press for 1 millisecond
            key = cv2.waitKey(1)

            # Check if key '1' is pressed
            if key == ord('1'):
                cv2.destroyAllWindows()  # Close all OpenCV windows
                cap.release()  # Release the webcam
                return HttpResponse("Camera stopped. Thank you for using the webcam!")

            # Check if the 'Esc' key is pressed
            elif key == 27:  # 27 is the ASCII code for 'Esc' key
                break

        # Release the webcam and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

    return render(request , "FaceDetection/FaceDetection_second.html" )
