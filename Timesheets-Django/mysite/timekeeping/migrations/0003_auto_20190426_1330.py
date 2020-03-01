# Generated by Django 2.2 on 2019-04-26 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timekeeping', '0002_auto_20190417_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='dimprojects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField()),
                ('client', models.CharField(max_length=200)),
                ('project_name', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='edgered_timesheets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hours_worked', models.IntegerField()),
                ('timecode', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('islatest', models.IntegerField()),
                ('date_changed', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='dimemployees',
            name='active',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='dimemployees',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dimemployees',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]