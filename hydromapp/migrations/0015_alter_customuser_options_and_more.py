# Generated by Django 4.2.5 on 2024-02-10 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydromapp', '0014_customuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={},
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='contact_number',
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default='0784165655', max_length=10),
        ),
    ]