# Generated by Django 2.2 on 2021-11-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_bookdata_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdata',
            name='book_image',
            field=models.ImageField(default='images/none/nnoimg.jpg', upload_to='images'),
        ),
    ]
