# Generated by Django 3.1.7 on 2021-03-22 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='offer',
            new_name='flag',
        ),
    ]
