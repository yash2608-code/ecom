# Generated by Django 2.0 on 2021-08-06 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(default='Email', max_length=100)),
                ('passwd', models.CharField(default='Password', max_length=100)),
                ('Role', models.CharField(default='Role', max_length=100)),
                ('Fotp', models.BigIntegerField(default=123456)),
                ('Is_Created', models.DateTimeField(auto_now_add=True)),
                ('Is_Activated', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(default='Seller Firstname', max_length=100)),
                ('Lastname', models.CharField(default='Seller Lastname', max_length=100)),
                ('Address', models.CharField(default='Seller Address', max_length=100)),
                ('phone', models.BigIntegerField(default=123456790)),
                ('bdate', models.DateField(auto_now_add=True)),
                ('Gender', models.CharField(default='Seller Gender', max_length=100)),
                ('Admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(default='Firstname', max_length=100)),
                ('Lastname', models.CharField(default='Lastname', max_length=100)),
                ('Address', models.CharField(default='Address', max_length=100)),
                ('phone', models.BigIntegerField(default=123456790)),
                ('bdate', models.DateField(auto_now_add=True)),
                ('Gender', models.CharField(default='Gender', max_length=100)),
                ('Admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Admin')),
            ],
        ),
    ]
