# Generated by Django 5.2 on 2025-06-01 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ortsteil',
            field=models.CharField(choices=[('Bu', 'Buckau'), ('Wi', 'Wittstock'), ('Dr', 'Dretzen'), ('St', 'Steinberg')], default='Bu', max_length=200, verbose_name='Ortsteil'),
        ),
    ]
