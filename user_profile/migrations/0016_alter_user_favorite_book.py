# Generated by Django 4.2.6 on 2023-10-28 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0015_alter_user_favorite_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorite_book',
            field=models.JSONField(default=dict),
        ),
    ]