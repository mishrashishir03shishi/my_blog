# Generated by Django 3.0.2 on 2020-04-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0025_auto_20200418_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
