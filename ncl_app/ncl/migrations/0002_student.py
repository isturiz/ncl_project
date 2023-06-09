# Generated by Django 4.1.7 on 2023-03-14 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ncl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('age_category', models.CharField(choices=[('A', '3 to 5 years old'), ('B', '6 to 9 years old'), ('C', '10 to 12 years old')], max_length=1)),
                ('representative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ncl.representative')),
            ],
        ),
    ]
