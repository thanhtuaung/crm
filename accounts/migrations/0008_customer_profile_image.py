# Generated by Django 4.2.4 on 2023-08-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
