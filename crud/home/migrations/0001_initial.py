# Generated by Django 2.2.12 on 2022-04-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='entry',
            fields=[
                ('ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('data1', models.CharField(max_length=100)),
                ('data2', models.CharField(max_length=100)),
            ],
        ),
    ]
