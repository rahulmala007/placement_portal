# Generated by Django 2.2.6 on 2019-11-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20191106_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
