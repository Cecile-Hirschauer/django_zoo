# Generated by Django 3.0.5 on 2020-05-31 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0008_medicalvisit_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalvisit',
            name='title',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]