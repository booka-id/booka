# Generated by Django 4.2.6 on 2023-10-28 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_remove_user_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='images'),
        ),
    ]
