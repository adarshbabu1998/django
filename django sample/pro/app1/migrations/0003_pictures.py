# Generated by Django 4.2.1 on 2023-07-12 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_student_lname'),
    ]

    operations = [
        migrations.CreateModel(
            name='pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='mypics/')),
            ],
        ),
    ]
