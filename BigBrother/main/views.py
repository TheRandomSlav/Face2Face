from django.shortcuts import render

# Create your views here.
def is_video(file):
    try:
        clip = mp.VideoFileClip(file)
        return True
    except IOError:
        return False

def index(request):
    if request.method == 'POST' :
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['file']

            if is_video(file.temporary_file_path()):
                # Файл является видеозаписью
                return render(request, 'main/index.html') # Обработай и добавь данные

            else:
                # Файл не является видеозаписью
                return render(request, 'main/index.html')

    return render(request, 'main/index.html')