# Generated by Django 3.2 on 2021-06-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0018_alter_animal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enclosure',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
