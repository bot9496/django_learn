# Generated by Django 2.2.15 on 2020-09-12 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('pass1', models.CharField(max_length=100)),
                ('pass2', models.CharField(max_length=100)),
            ],
        ),
    ]