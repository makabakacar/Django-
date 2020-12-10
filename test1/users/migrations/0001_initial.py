# Generated by Django 2.2.5 on 2020-12-07 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='web_db1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=128)),
                ('age', models.IntegerField(default=18)),
                ('gender', models.BooleanField(default=False)),
                ('tel', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'web_db1',
            },
        ),
    ]
