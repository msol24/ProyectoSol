# Generated by Django 4.1.3 on 2022-11-23 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SolApp', '0004_wotp'),
    ]

    operations = [
        migrations.CreateModel(
            name='RHCP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicacion', models.DateField()),
                ('suscriptor', models.CharField(max_length=40)),
                ('critica', models.CharField(max_length=200)),
            ],
        ),
    ]