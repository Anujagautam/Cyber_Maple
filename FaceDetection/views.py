from django.shortcuts import render , redirect

# Create your views here.
from .models import Image
from .forms import ImageForm
from django.http import HttpResponse


def show(request):
    if request.method == "POST":
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
        
    form = ImageForm()
    img = Image.objects.all()

    last_image = Image.objects.last()


    

    form = ImageForm()
    return render (request , "FaceDetection/FaceDetection_first.html" , {'last_image':last_image , 'form':form})
    # return render(request, 'FaceDetection/FaceDetection_first.html')


