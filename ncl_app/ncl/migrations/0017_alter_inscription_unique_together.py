# Generated by Django 4.2.1 on 2023-05-23 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ncl', '0016_alter_inscription_student_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='inscription',
            unique_together=set(),
        ),
    ]