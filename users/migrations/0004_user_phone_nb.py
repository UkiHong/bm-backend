# Generated by Django 4.1.2 on 2022-12-24 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="phone_nb",
            field=models.CharField(default=False, max_length=15),
            preserve_default=False,
        ),
    ]
