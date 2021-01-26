# Generated by Django 3.1.5 on 2021-01-22 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0011_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='select',
            options={},
        ),
        migrations.RemoveField(
            model_name='question',
            name='categories',
        ),
        migrations.AddField(
            model_name='question',
            name='categories',
            field=models.ManyToManyField(to='generator.Select'),
        ),
        migrations.AlterField(
            model_name='select',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
