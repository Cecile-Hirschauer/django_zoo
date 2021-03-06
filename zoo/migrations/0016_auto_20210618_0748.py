# Generated by Django 3.2 on 2021-06-18 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0015_enclosure_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favanimal',
            name='fav_animal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='zoo.animal'),
        ),
        migrations.AddConstraint(
            model_name='favanimal',
            constraint=models.UniqueConstraint(fields=('reg_user', 'fav_animal'), name='unique_fav'),
        ),
    ]
