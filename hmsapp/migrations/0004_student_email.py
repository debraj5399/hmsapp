# Generated by Django 3.1.7 on 2021-04-11 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0003_remove_student_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
