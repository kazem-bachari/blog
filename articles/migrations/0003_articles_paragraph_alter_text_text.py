# Generated by Django 4.0 on 2021-12-28 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_articles_options_alter_text_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='paragraph',
            field=models.TextField(default=' ', verbose_name='متن '),
        ),
        migrations.AlterField(
            model_name='text',
            name='text',
            field=models.TextField(verbose_name='پاراگراف'),
        ),
    ]
