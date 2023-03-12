# Generated by Django 2.2.16 on 2022-04-24 10:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_auto_20220424_0758"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="follow",
            name="unique_follow",
        ),
        migrations.AddConstraint(
            model_name="follow",
            constraint=models.UniqueConstraint(
                fields=("user", "following"), name="unique_user_following"
            ),
        ),
    ]