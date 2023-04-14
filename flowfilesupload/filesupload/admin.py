from django.contrib import admin
from filesupload.models import UploadedFile

class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'mpan', 'files', 'reading', 'timestamp')
    list_filter = ('id', 'mpan')
    search_fields = ('id', 'mpan')  # Add search fields for id and filename



#admin.site.register(UploadedFile)
admin.site.register(UploadedFile, UploadedFileAdmin)
