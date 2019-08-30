# Generated by Django 2.2.4 on 2019-08-17 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.FloatField()),
                ('presion', models.FloatField()),
                ('humedad', models.FloatField()),
                ('monoxidoCarbono', models.FloatField()),
                ('fecha', models.DateField()),
                ('delegacion', models.CharField(max_length=50)),
            ],
        ),
    ]
