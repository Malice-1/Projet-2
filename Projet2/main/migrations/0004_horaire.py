# Generated by Django 5.0.6 on 2024-11-21 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_movie_movieselection_ticket_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
            ],
        ),
    ]
