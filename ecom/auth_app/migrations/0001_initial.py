# Generated by Django 4.1.7 on 2023-02-22 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]