# Generated by Django 5.0.1 on 2024-01-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='CrawlingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_id', models.CharField(max_length=255)),
                ('images', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image_files', models.ManyToManyField(blank=True, related_name='logs', to='crawlingApp.imagefile')),
            ],
        ),
    ]
