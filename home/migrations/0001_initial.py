# Generated by Django 3.1.4 on 2021-01-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=10)),
                ('about', models.CharField(max_length=25)),
                ('dateTime', models.DateTimeField()),
                ('subDateTime', models.DateTimeField()),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
