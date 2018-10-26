# Generated by Django 2.1.2 on 2018-10-26 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0005_auto_20181019_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='description',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.URLField(),
        ),
    ]