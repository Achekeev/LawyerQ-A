# Generated by Django 3.2.7 on 2021-09-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210914_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]