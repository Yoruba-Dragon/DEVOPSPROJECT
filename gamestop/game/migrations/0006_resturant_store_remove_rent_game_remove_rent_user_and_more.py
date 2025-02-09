# Generated by Django 5.0.3 on 2024-04-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_rent_rent_date_alter_rent_rented'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resturant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resturantname', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=250, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('resturant_pic', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('openingtime', models.TimeField(max_length=30)),
                ('closingtime', models.TimeField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storename', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=250, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('store_pic', models.ImageField(blank=True, null=True, upload_to='static/images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('openingtime', models.TimeField(max_length=30)),
                ('closingtime', models.TimeField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='rent',
            name='game',
        ),
        migrations.RemoveField(
            model_name='rent',
            name='user',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='Rent',
        ),
    ]
