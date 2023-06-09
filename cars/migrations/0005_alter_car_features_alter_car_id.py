# Generated by Django 4.1.7 on 2023-05-13 08:15

import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0004_auto_20230317_1640"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="features",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("Cruise Control", "Cruise Control"),
                    ("Audio Interface", "Audio Interface"),
                    ("Airbags", "Airbags"),
                    ("Air Conditioning", "Air Conditioning"),
                    ("Seat Heating", "Seat Heating"),
                    ("Alarm System", "Alarm System"),
                    ("ParkAssist", "ParkAssist"),
                    ("Power Steering", "Power Steering"),
                    ("Reversing Camera", "Reversing Camera"),
                    ("Direct Fuel Injection", "Direct Fuel Injection"),
                    ("Auto Start/Stop", "Auto Start/Stop"),
                    ("Wind Deflector", "Wind Deflector"),
                    ("Bluetooth Handset", "Bluetooth Handset"),
                ],
                max_length=195,
                validators=[django.core.validators.MaxValueValidator(10)],
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
