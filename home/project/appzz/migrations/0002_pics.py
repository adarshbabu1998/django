# Generated by Django 4.2.2 on 2023-06-19 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appzz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p', models.ImageField(upload_to='mypics/')),
            ],
        ),
    ]
