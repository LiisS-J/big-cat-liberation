# Generated by Django 3.2.6 on 2021-08-25 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210824_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='pending',
            field=models.CharField(choices=[('Pending', 'Pending...'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Pending', max_length=8),
        ),
    ]
