from django.shortcuts import render, redirect, get_object_or_404
from .forms import CollageForm
from .models import Collage, ImageItem
from .models import UploadedImage

def upload_images(request):
    if request.method == 'POST':
        for f in request.FILES.getlist('images'):
            UploadedImage.objects.create(image=f)
        return redirect('select_images')
    return render(request, 'collage_app/upload_images.html')



def select_images(request):
    images = UploadedImage.objects.all()
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_images')
        selected_images = UploadedImage.objects.filter(id__in=selected_ids)
        collage_type = request.POST.get('collage_type')
        return render(request, 'collage_app/generated_collage.html', {
            'selected_images': selected_images,
            'collage_type': collage_type
        })
    return render(request, 'collage_app/select_images.html', {'images': images})



def upload_collage(request):
    if request.method == 'POST':
        form = CollageForm(request.POST, request.FILES)
        if form.is_valid():
            collage = Collage.objects.create(title=form.cleaned_data['title'])
            for img in request.FILES.getlist('images'):
                ImageItem.objects.create(collage=collage, image=img)
            return redirect('collage_detail', pk=collage.pk)
    else:
        form = CollageForm()
    return render(request, 'collage_app/upload.html', {'form': form})


def collage_detail(request, pk):
    collage = get_object_or_404(Collage, pk=pk)
    return render(request, 'collage_app/collage_detail.html', {'collage': collage})


def collage_list(request):
    collages = Collage.objects.all().order_by('-created_at')
    return render(request, 'collage_app/collage_list.html', {'collages': collages})