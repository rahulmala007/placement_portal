# Generated by Django 2.2.6 on 2019-10-31 12:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_branchnumberplaced'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchName', models.CharField(default='', max_length=50)),
                ('num', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayNum', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('num', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Branch')),
            ],
        ),
        migrations.DeleteModel(
            name='BranchNumberPlaced',
        ),
        migrations.AddField(
            model_name='student',
            name='day',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Branch'),
        ),
    ]