from django.db import models


# Create your models here.
class BookData(models.Model):

    def __str__(self):
        return self.book_name

    book_name = models.CharField(max_length=200)
    book_category = models.CharField(max_length=200)
    book_description = models.CharField(max_length=500)
    book_rating = models.FloatField()
    book_image = models.ImageField(upload_to='images', default='images/none/nnoimg.jpg')

