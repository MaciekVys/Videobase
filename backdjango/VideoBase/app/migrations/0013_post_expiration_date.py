# Generated by Django 5.0.3 on 2024-04-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_post_expiration_date_post_dislikes_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='expiration_date',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]