# Generated by Django 3.1.5 on 2021-01-23 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0017_select_orden'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='orden',
            field=models.IntegerField(blank=True, null=True, verbose_name='orden'),
        ),
    ]