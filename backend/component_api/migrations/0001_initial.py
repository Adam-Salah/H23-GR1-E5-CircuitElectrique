# Generated by Django 4.1.7 on 2023-03-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position_x', models.FloatField()),
                ('position_y', models.FloatField()),
                ('size', models.FloatField()),
                ('voltage', models.FloatField()),
                ('resistance', models.FloatField()),
                ('capacitance', models.FloatField()),
            ],
        ),
    ]
