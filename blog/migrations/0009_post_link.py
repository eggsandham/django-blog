# Generated by Django 2.0.8 on 2018-08-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_post_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
