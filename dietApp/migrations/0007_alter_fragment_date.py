# Generated by Django 3.2.7 on 2022-01-02 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietApp', '0006_alter_fragment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fragment',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
