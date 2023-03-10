# Generated by Django 4.1.6 on 2023-02-05 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('birth', models.DateTimeField(verbose_name='date published')),
                ('age', models.IntegerField()),
            ],
        ),
    ]
