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


# CSV Work Flow 
import pandas as pd
df = pd.read_csv("database_info/Cyber_Crime_DataSet.csv"  , encoding='unicode_escape')
label = ['Aamir Khan', 'Abhay Deol', 'Abhishek Bachchan', 'Ajay Devgn', 'Ameesha_Patel', 'Arshad_Warsi', 'Mahendra Singh Pansingh Dhoni', 'Mrunal_Thakur', 'Narendra Damodardas Modi']
label[0]
series = list(df['Name'])



import matplotlib.pyplot as plt
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

    image_name = last_image.photo.name.split('/')[-1] if last_image else None

    up_last_img  = str('media/myimage/'+image_name)
    # print("last Image show " , up_last_img)
    form = ImageForm()


    
    img = cv2.imread(up_last_img)
    # print(img)
    imgs = cv2.resize(img , (0 , 0 ) , None , 0.25 ,0.25)
    imgs = cv2.cvtColor(img , cv2.COLOR_RGB2BGR)
    # print(imgs)

    # Model Work Flow
    final_name = ""
    facescurframe = face_recognition.face_locations(imgs)
    encodescurframe = face_recognition.face_encodings(imgs , facescurframe)
    for encodeface , faceloc in zip(encodescurframe , facescurframe):
                matches = face_recognition.compare_faces(encodelistknown , encodeface)

                facedis = face_recognition.face_distance(encodelistknown , encodeface)

                print(facedis)

                matchindex = np.argmin(facedis)

                if matches[matchindex]:
                    final_name = classname[matchindex].upper()
                    print(final_name)

    #My Data Base inside 
    name = list(os.listdir("database_images"))
    list_name = list(name)

    for i in range(len(list_name)):
        list_name[i] = list_name[i][:4]
    print(list_name)

    # CSV File Code
    fir , sec ,thi ,fou , fiv,six ,sev , eig , nine ,ten = "" , "" , "" , "" , "" , "" , "" , "" , "" ,""
    for i in range(len(series)):
        actual_name = series[i]
        actual_name = actual_name[:4]
        if str(actual_name).lower() == str(final_name[:4]).lower():
            all = list(df.iloc[i])
            fir = all[0]
            sec = all[1]
            thi = all[2]
            fou = all[3]
            fiv = all[4]
            six = all[5]
            sev = all[6]
            eig = all[7]
            nine = all[8]
            ten = str(all[9])
            print("Final" , ten)
            break
            

    ten  = 'FaceDetection/images/Aamir Khan.jpg'
    img = cv2.imread(ten)
    print("Hello" , img)
    ten  = 'FaceDetection/images/Aamir Khan.jpg'




    return render (request , "FaceDetection/FaceDetection_first.html" , {'last_image':last_image , 'form':form  , 'final_name':final_name , 'fir':fir , 'sec':sec , 'thi':thi ,'fou':fou ,'fiv':fiv , 'six':six , 'sev':sev , 'eig':eig , 'nine':nine ,'ten':ten})
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

    return render(request , "FaceDetection/video.html" )




