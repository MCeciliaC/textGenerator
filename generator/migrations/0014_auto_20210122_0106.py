# Generated by Django 3.1.5 on 2021-01-22 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0013_auto_20210122_0102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='select',
            old_name='categories',
            new_name='questions',
        ),
    ]