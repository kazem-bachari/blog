# Generated by Django 4.0 on 2021-12-28 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articles_paragraph_alter_text_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
    ]
