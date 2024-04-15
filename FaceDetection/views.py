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
    last_image = None
    final_name = ""
    fir, sec, thi, fou, fiv, six, sev, eig, nine, ten = "", "", "", "", "", "", "", "", "", ""
    
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            last_image = Image.objects.last()
            if last_image:
                image_name = last_image.photo.name.split('/')[-1]
                up_last_img = f'media/myimage/{image_name}'
                img = cv2.imread(up_last_img)
                imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
                imgs = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                facescurframe = face_recognition.face_locations(imgs)
                encodescurframe = face_recognition.face_encodings(imgs, facescurframe)
                for encodeface, faceloc in zip(encodescurframe, facescurframe):
                    matches = face_recognition.compare_faces(encodelistknown, encodeface)
                    facedis = face_recognition.face_distance(encodelistknown, encodeface)
                    matchindex = np.argmin(facedis)
                    if matches[matchindex]:
                        final_name = classname[matchindex].upper()
                        break
            
            # Fetch data from CSV file based on the detected name
            if final_name:
                actual_name = final_name[:4]
                for i in range(len(series)):
                    if str(series[i]).lower()[:4] == str(actual_name).lower():
                        all_data = list(df.iloc[i])
                        fir, sec, thi, fou, fiv, six, sev, eig, nine, ten = all_data
                        ten = f'FaceDetection/images/{ten}'
                        break
        
    else:
        # Reset variables when the page is loaded via GET request
        form = ImageForm()
        last_image = None
        final_name = ""
        fir, sec, thi, fou, fiv, six, sev, eig, nine, ten = "", "", "", "", "", "", "", "", "", ""
    
    return render(request, "FaceDetection/FaceDetection_first.html", {'last_image': last_image, 'form': form,
                                                                    'final_name': final_name, 'fir': fir,
                                                                    'sec': sec, 'thi': thi, 'fou': fou, 'fiv': fiv,
                                                                    'six': six, 'sev': sev, 'eig': eig, 'nine': nine,
                                                                    'ten': ten})





def video_show(request):
    return render(request, "FaceDetection/video.html")
from django.http import StreamingHttpResponse
from django.shortcuts import render
import cv2
import threading

# VideoCamera class to capture video
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        self.streaming = True  # Flag to control streaming
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        cv2.putText(image, "sachin", (50+6, 50-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255,), 2)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while self.streaming:
            (self.grabbed, self.frame) = self.video.read()

# Function to generate video frames
def gen(camera):
    while camera.streaming:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# View function to render the video page and start video detection
def video_show(request):
    return render(request, 'FaceDetection/video.html')

# Decorated view function for video streaming with gzip compression
def videoshow(request):
    cam = VideoCamera()
    response = StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    return response













# ------------------------------------------------------------------------------------------------------------------
# def video_show(request):
#     if request.method == "POST":

#         cap = cv2.VideoCapture(0)

#         # Check if the webcam is opened successfully
#         if not cap.isOpened():
#             return HttpResponse("Error: Unable to open webcam")

#         # Loop to capture frames from the webcam
#         while True:
#             # Read frame from the webcam
#             success  , img = cap.read()
            
#             # Check if the frame is read successfully
#             if not success:
#                 return HttpResponse("Error: Unable to read frame from webcam")
#             imgs = cv2.resize(img , (0 , 0 ) , None , 0.25 ,0.25)
#             imgs = cv2.cvtColor(imgs , cv2.COLOR_RGB2BGR)

#             # Model Work Flow

#             facescurframe = face_recognition.face_locations(imgs)
#             encodescurframe = face_recognition.face_encodings(imgs , facescurframe)


#             for encodeface , faceloc in zip(encodescurframe , facescurframe):
#                 matches = face_recognition.compare_faces(encodelistknown , encodeface)

#                 facedis = face_recognition.face_distance(encodelistknown , encodeface)

#                 print(facedis)

#                 matchindex = np.argmin(facedis)

#                 if matches[matchindex]:
#                     name = classname[matchindex].upper()
#                     print(name)

#                     y1 , x2 , y2 , x1 = faceloc
#                     y1 , x2 , y2 , x1  = y1*4 , x2*4 , y2*4 , x1*4 
#                     cv2.rectangle(img , (x1 , y1) , (x2 , y2) , (0,255,0),2)
#                     cv2.rectangle(img , (x1 , y2-35) , (x2 , y2) , (0,255,0),cv2.FILLED)
#                     cv2.putText(img  ,name, (x1+6 , y2-6) , cv2.FONT_HERSHEY_COMPLEX, 1 , (255  , 255, 255,) ,2)



#             # Display the frame
#             cv2.imshow("WebCam Image", img)


            

#             # Wait for a key press for 1 millisecond
#             key = cv2.waitKey(1)

#             # Check if key '1' is pressed
#             if key == ord('1'):
#                 cv2.destroyAllWindows()  # Close all OpenCV windows
#                 cap.release()  # Release the webcam
#                 return HttpResponse("Camera stopped. Thank you for using the webcam!")

#             # Check if the 'Esc' key is pressed
#             elif key == 27:  # 27 is the ASCII code for 'Esc' key
#                 break

#         # Release the webcam and close all OpenCV windows
#         cap.release()
#         cv2.destroyAllWindows()

#     return render(request , "FaceDetection/video.html" )


