# Generated by Django 3.0.2 on 2020-04-16 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20200417_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(choices=[('1', 'Science'), ('2', 'Tech'), ('3', 'Polity'), ('4', 'Miscellaneous')], default='4', on_delete=django.db.models.deletion.CASCADE, to='articles.Category'),
        ),
    ]
