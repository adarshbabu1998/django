# Generated by Django 4.2.2 on 2023-06-19 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appzz', '0002_pics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pics',
            old_name='p',
            new_name='img',
        ),
    ]
