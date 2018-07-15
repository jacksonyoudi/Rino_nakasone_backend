from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    score = models.CharField(max_length=100)
    img_url = models.CharField(max_length=1024)
    download_url = models.CharField(max_length=1024)
    introduction = models.CharField(max_length=2048)
    author_info = models.CharField(max_length=2048)
    directory = models.CharField(max_length=4096)
    create_edit = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = "ireadweek"
