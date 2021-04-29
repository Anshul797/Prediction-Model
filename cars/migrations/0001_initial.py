# Generated by Django 2.1.7 on 2019-10-20 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('seller', models.CharField(choices=[('privat', 'privat'), ('gewerblich', 'gewerblich')], max_length=50)),
                ('offerType', models.CharField(choices=[('Angebot', 'Angebot'), ('Gesuch', 'Gesuch')], max_length=50)),
                ('abtest', models.CharField(choices=[('test', 'test'), ('control', 'control')], max_length=50)),
                ('vehicleType', models.CharField(max_length=50)),
                ('yearOfRegistration', models.IntegerField()),
                ('gearbox', models.CharField(choices=[('manuell', 'manuell'), ('automatik', 'automatik')], max_length=50)),
                ('powerPS', models.IntegerField()),
                ('model', models.CharField(max_length=50)),
                ('kilometer', models.IntegerField()),
                ('monthOfRegistration', models.IntegerField()),
                ('fuelType', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('notRepairedDamage', models.CharField(choices=[('nein', 'nein'), ('ja', 'ja')], max_length=50)),
                ('postalCode', models.IntegerField()),
                ('nrOfPictures', models.IntegerField()),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
