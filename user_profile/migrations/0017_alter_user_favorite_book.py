# Generated by Django 4.2.6 on 2023-10-29 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0016_alter_user_favorite_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorite_book',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]