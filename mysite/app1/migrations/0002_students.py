# Generated by Django 4.2.1 on 2023-06-01 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField()),
                ('standard', models.SmallIntegerField()),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
