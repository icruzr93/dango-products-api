# Generated by Django 2.2.2 on 2019-06-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('position', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('image', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=120)),
            ],
        ),
    ]
