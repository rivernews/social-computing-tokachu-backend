# Generated by Django 2.1.3 on 2018-11-19 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('min_lat', models.FloatField()),
                ('max_lat', models.FloatField()),
                ('min_lon', models.FloatField()),
                ('max_lon', models.FloatField()),
                ('description', models.TextField()),
                ('place_photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Pictures')),
            ],
        ),
    ]
