# Generated by Django 2.0 on 2021-09-13 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_admin_t_c'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=10)),
            ],
        ),
    ]