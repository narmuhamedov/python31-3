# Generated by Django 4.2.4 on 2023-08-24 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_stars', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car_rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_object', to='cars.cars')),
            ],
        ),
    ]
