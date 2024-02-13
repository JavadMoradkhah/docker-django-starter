from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm


def home(request):
    return HttpResponse('Home Page')


def upload_file(request):
    form = UploadFileForm()

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES["file"]
            storage = FileSystemStorage()
            storage.save(file.name, file)
            return HttpResponse("File uploaded successfully")

    return render(request, 'core/index.html', {'form': form})
