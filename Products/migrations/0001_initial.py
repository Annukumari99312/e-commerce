# Generated by Django 3.0.5 on 2020-04-10 19:00

import Products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=4, default=39.99, max_digits=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to=Products.models.upload_image_path)),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'products',
                'verbose_name_plural': 'Product',
            },
        ),
    ]
