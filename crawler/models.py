from django.db import models

class PDFFile(models.Model):
    file = models.FileField(upload_to='pdf_files/')
    filename = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.filename
