# Generated by Django 2.2 on 2021-11-01 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0003_auto_20211101_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdata',
            name='book_genre',
        ),
    ]