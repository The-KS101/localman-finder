# Generated by Django 3.0.5 on 2020-04-24 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0003_place_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='places', to='finder.Category'),
        ),
    ]