# Generated by Django 3.0.2 on 2020-04-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_remove_article_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('1', 'Science'), ('2', 'Tech'), ('3', 'Polity'), ('4', 'Miscellaneous')], default='4', max_length=20),
        ),
    ]
