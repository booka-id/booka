# Generated by Django 4.2.6 on 2023-10-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='C:\\Users\\Syarief\\Documents\\UI\\Semester-3\\PBP\\tugas_kelompok\\static/userprofile/default.png', null=True, upload_to='profile_pics/'),
        ),
    ]