# Generated by Django 2.0 on 2021-09-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_name',
            field=models.CharField(max_length=200),
        ),
    ]
