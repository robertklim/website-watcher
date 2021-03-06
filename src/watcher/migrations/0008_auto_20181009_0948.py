# Generated by Django 2.1.2 on 2018-10-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0007_auto_20181009_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitecheck',
            name='error',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='websitecheck',
            name='result',
            field=models.CharField(blank=True, choices=[('OK', 'Ok'), ('ALERT', 'Alert'), ('ERROR', 'Error'), (None, 'None')], max_length=128),
        ),
    ]
