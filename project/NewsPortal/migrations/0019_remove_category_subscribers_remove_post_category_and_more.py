# Generated by Django 4.2 on 2023-05-10 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortal', '0018_rename_categories_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subscribers',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='PostCategory',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='music', max_length=255),
        ),
    ]
