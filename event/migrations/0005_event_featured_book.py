# Generated by Django 4.2.6 on 2023-10-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_event_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='featured_book',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]