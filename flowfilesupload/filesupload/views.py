from django.shortcuts import render
from .forms import UploadFileForm
from django.views.decorators.csrf import ensure_csrf_cookie
import csv
import datetime

from .models import UploadedFile


@ensure_csrf_cookie
def upload_file(request):
    if request.method == 'POST':
        for file in request.FILES.getlist('files'):
            # Open the file in text mode using the encoding parameter
            with open(file.name, 'r', encoding='utf-8') as f:
                reader = csv.reader(f, delimiter='|')
                for row in reader:
                    if row[0] == 'ZHV':
                        continue  # Ignore header row
                    if row[0] == '026':
                        mpan = row[1]

                    if row[0] == '030':
                        timestamp_str = row[2]
                        timestamp = datetime.datetime.strptime(timestamp_str, '%Y%m%d%H%M%S%f')
                    else:
                        continue

                    UploadedFile.objects.create(
                        reading=float(row[3]),
                        timestamp=timestamp,
                        mpan=mpan,
                        files=file.name
                    )
                handle_uploaded_file(file)
        context = {'msg': 'File successfully uploaded'}
        return render(request, "index.html", context)
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})
    
def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

