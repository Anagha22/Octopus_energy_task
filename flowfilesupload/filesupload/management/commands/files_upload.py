from django.core.files.uploadedfile import UploadedFile
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File

import os


class Command(BaseCommand):
    help = "Uploads file to the database"

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Path to the file to upload')

    def handle(self, *args, **options):
        path = options['path']
        if os.path.exists(path):
            with open(path, 'rb') as f:
                uploaded_file = UploadedFile(file=File(f))
                self.stdout.write(self.style.SUCCESS('Successfully uploaded file "%s"' % uploaded_file.file.name))
        else:
                self.stderr.write(self.style.ERROR('File does not exist'))
