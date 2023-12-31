# Generated by Django 4.2.4 on 2023-12-19 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20231026_1401'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0002_auto_20231123_0740'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('payment_method', models.CharField(max_length=30)),
                ('purchase_time', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
