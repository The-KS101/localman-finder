# Generated by Django 3.0.5 on 2020-04-26 00:22

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0005_place_date_stamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=120)),
                ('lname', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures/%Y/%m/%d/')),
                ('message', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]