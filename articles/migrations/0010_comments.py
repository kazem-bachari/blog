# Generated by Django 4.0 on 2022-01-08 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('articles', '0009_rename_article_articles_catagorize'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('text', models.TextField(max_length=300)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.user')),
            ],
        ),
    ]
