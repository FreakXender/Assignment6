from django.shortcuts import render, redirect
from .forms import MediaFileForm
from .models import MediaFile

def upload_media(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = MediaFileForm()
    return render(request, 'mediafiles/upload.html', {'form': form})

def media_list(request):
    media_files = MediaFile.objects.all().order_by('-uploaded_at')
    return render(request, 'mediafiles/list.html', {'media_files': media_files})

