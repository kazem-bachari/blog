# Generated by Django 4.0 on 2021-12-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterModelOptions(
            name='text',
            options={'verbose_name': 'پارگراف ها', 'verbose_name_plural': 'متن'},
        ),
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]