# Generated by Django 4.1.2 on 2022-12-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0002_alter_booking_experience_alter_booking_room_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="not_canceled",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
