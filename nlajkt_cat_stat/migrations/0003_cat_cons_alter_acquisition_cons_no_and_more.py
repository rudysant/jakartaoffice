# Generated by Django 4.1.1 on 2022-10-28 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nlajkt_cat_stat", "0002_trip_place_rename_acquisition2_acquisition_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cat_cons",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("consign_no", models.IntegerField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("new_itle", models.IntegerField()),
                ("add_vol", models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name="acquisition",
            name="cons_no",
            field=models.IntegerField(default=462),
        ),
        migrations.AlterField(
            model_name="catalogues",
            name="consignment_no",
            field=models.IntegerField(default=462),
        ),
    ]
