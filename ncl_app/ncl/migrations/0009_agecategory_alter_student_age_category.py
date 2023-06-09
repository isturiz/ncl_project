# Generated by Django 4.1.7 on 2023-03-26 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ncl', '0008_remove_inscription_section_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='age_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ncl.agecategory'),
        ),
    ]
