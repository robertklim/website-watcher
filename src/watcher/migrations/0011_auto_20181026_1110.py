# Generated by Django 2.1.2 on 2018-10-26 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0010_auto_20181026_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitechecksettings',
            name='website_hash',
            field=models.CharField(max_length=128),
        ),
    ]
