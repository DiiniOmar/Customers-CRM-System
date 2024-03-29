# Generated by Django 5.0.1 on 2024-03-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Created_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=92)),
                ('last_name', models.CharField(max_length=92)),
                ('email', models.CharField(max_length=92)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=200)),
                ('county', models.CharField(max_length=300)),
            ],
        ),
    ]
