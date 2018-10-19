# Generated by Django 2.1.2 on 2018-10-19 10:30

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('websites', '0004_auto_20181009_0943'),
        ('watcher', '0008_auto_20181009_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteCheckSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_hash', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('dom_exclusions', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websites.Website')),
            ],
        ),
        migrations.AlterField(
            model_name='websitecheck',
            name='website_settings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='website_checks', to='watcher.WebsiteCheckSettings'),
        ),
    ]
