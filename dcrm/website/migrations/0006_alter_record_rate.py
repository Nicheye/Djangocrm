# Generated by Django 4.1.7 on 2023-04-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_record_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='rate',
            field=models.IntegerField(),
        ),
    ]
