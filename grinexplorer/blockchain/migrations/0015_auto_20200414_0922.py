# Generated by Django 2.1.1 on 2020-04-14 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0014_auto_20191202_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='timestamp',
            field=models.DateTimeField(db_index=True),
        ),
    ]