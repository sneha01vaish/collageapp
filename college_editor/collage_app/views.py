from django.shortcuts import render, redirect, get_object_or_404
from .forms import CollageForm
from .models import Collage, ImageItem
from .models import UploadedImage

def home(request):
    return render(request, 'collage_app/home.html')

def upload_images(request):
    if request.method == 'POST':
        for f in request.FILES.getlist('images'):
            UploadedImage.objects.create(image=f)
        return redirect('select_images')
    return render(request, 'collage_app/upload_images.html')



def select_images(request):
    images = UploadedImage.objects.all()
    if not images.exists():
        return render(request, 'collage_app/no_images.html')

    error = None

    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_images')
        collage_type = request.POST.get('collage_type')

        # Convert collage_type to int safely
        try:
            collage_type_int = int(collage_type)
        except (ValueError, TypeError):
            error = "Please select a valid collage type."
            collage_type_int = None

        if collage_type_int and len(selected_ids) != collage_type_int:
            error = f"You selected {len(selected_ids)} images but chose {collage_type_int} pics collage."

        if error:
            # Send back error message and previously selected values
            return render(request, 'collage_app/select_images.html', {
                'images': images,
                'error': error,
                'selected_ids': list(map(int, selected_ids)),
                'selected_collage_type': collage_type,
            })

        selected_images = UploadedImage.objects.filter(id__in=selected_ids)
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
