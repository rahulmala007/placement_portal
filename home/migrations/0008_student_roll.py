# Generated by Django 2.1 on 2019-11-05 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191031_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roll',
            field=models.CharField(default=180101000, max_length=50),
            preserve_default=False,
        ),
    ]