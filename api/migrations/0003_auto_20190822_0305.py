# Generated by Django 2.2.3 on 2019-08-22 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190815_0004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='doctor',
            new_name='patient',
        ),
        migrations.DeleteModel(
            name='SignedPrescription',
        ),
    ]
