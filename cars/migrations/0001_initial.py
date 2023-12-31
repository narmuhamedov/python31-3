# Generated by Django 4.2.4 on 2023-08-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='cars/')),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=100)),
                ('type_car', models.CharField(choices=[('Олдовые', 'Олдовые'), ('Спортивные', 'Спортивные'), ('Грузовые', 'Грузовые')], max_length=100)),
                ('url_car', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
