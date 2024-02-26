# Generated by Django 5.0 on 2024-02-26 12:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('productImg', models.ImageField(upload_to='product_images/')),
                ('productTitle', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', models.CharField(max_length=10)),
                ('color', models.JSONField()),
                ('size', models.JSONField()),
                ('stock', models.IntegerField()),
                ('orders', models.IntegerField()),
                ('publish', models.DateTimeField()),
            ],
        ),
    ]