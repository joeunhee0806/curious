# Generated by Django 2.0.6 on 2018-07-02 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20180702_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='boardtitle',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Board'),
        ),
    ]
