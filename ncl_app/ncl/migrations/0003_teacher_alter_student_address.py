# Generated by Django 4.1.7 on 2023-03-15 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncl', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]
