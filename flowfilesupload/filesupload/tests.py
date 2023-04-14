from django.test import TestCase, Client
from django.urls import reverse
from filesupload.models import UploadedFile

class UploadedFileTestCase(TestCase):
    def setUp(self):
        # create an UploadedFile object for testing
        self.uploaded_file = UploadedFile.objects.create(
            reading=123.45,
            timestamp='2022-01-01 12:00:00',
            mpan=20000554331111,
            files='DTC5259515123502080915D0010.uff'
        )

    def test_upload_file(self):
        # test that the uploaded file exists in the database
        uploaded_file = UploadedFile.objects.get(reading=123.45)
        self.assertEqual(uploaded_file.timestamp, '2022-01-01 12:00:00')

