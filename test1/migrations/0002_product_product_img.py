# Generated by Django 5.0.7 on 2024-07-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test1", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_img",
            field=models.ImageField(default=1, upload_to="image/"),
            preserve_default=False,
        ),
    ]
