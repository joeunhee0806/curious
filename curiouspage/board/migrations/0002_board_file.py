# Generated by Django 2.0.6 on 2018-07-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]