# Generated by Django 4.1.5 on 2023-01-21 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('address', models.TextField(max_length=256)),
                ('whatsapp', models.CharField(max_length=15)),
                ('mobile_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('cnic', models.IntegerField()),
                ('profession', models.CharField(default='', max_length=256)),
                ('organization', models.CharField(default='', max_length=256)),
                ('designation', models.CharField(default='', max_length=256)),
                ('monthly_income', models.IntegerField()),
                ('working_since', models.DateField(default='')),
                ('qualification', models.CharField(default='', max_length=256)),
            ],
        ),
    ]
