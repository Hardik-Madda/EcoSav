# Generated by Django 4.1.3 on 2022-12-02 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BloggingApp', '0002_addpost1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post1', models.IntegerField()),
                ('Name', models.CharField(max_length=128)),
                ('Write_Post', models.TextField()),
                ('add_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='BloggingApp.addpost1')),
            ],
        ),
    ]