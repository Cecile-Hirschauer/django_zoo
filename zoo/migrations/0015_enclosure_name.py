# Generated by Django 3.2 on 2021-06-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0014_favanimal'),
    ]

    operations = [
        migrations.AddField(
            model_name='enclosure',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
