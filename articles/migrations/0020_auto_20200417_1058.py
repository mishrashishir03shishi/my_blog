# Generated by Django 3.0.2 on 2020-04-17 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_auto_20200417_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='categorize',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
