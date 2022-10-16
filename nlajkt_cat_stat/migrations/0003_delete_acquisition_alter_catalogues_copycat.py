# Generated by Django 4.0.6 on 2022-10-16 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlajkt_cat_stat', '0002_acquisition_book_source_consignment_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Acquisition',
        ),
        migrations.AlterField(
            model_name='catalogues',
            name='copycat',
            field=models.CharField(choices=[('No', 'No'), ('Partial copycat', 'Partial copycat'), ('Full copycat', 'Full copycat')], default='No', max_length=20),
        ),
    ]