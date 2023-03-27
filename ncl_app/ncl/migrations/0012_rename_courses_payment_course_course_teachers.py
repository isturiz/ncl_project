# Generated by Django 4.1.7 on 2023-03-27 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncl', '0011_representative_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='courses',
            new_name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(to='ncl.teacher'),
        ),
    ]