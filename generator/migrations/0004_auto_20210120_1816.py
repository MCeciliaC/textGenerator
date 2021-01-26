# Generated by Django 3.1.5 on 2021-01-20 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0003_auto_20200922_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Select',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Select acerca de',
            },
        ),
        migrations.AlterField(
            model_name='question',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.select'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]