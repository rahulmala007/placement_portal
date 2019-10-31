# Generated by Django 2.2.6 on 2019-10-31 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20191031_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='programs',
            field=models.CharField(choices=[('BTech', 'Bachelor of Technology'), ('BDes', 'Bachelor of Design'), ('MTech', 'Master of Technology'), ('MDes', 'Master of Design')], default='BTech', max_length=5),
        ),
    ]
