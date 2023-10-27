# Generated by Django 4.2.6 on 2023-10-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20231025_0739'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='book',
        ),
        migrations.AddField(
            model_name='cart',
            name='book',
            field=models.ManyToManyField(to='book.book'),
        ),
    ]
