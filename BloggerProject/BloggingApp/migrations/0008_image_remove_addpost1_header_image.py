# Generated by Django 4.1.3 on 2022-12-03 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloggingApp', '0007_rename_image_addpost1_header_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='addpost1',
            name='header_image',
        ),
    ]
