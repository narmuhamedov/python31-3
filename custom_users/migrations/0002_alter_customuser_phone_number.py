# Generated by Django 4.2.4 on 2023-08-31 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default='+996', max_length=13, null=True),
        ),
    ]