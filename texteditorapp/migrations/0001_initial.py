# Generated by Django 3.2.5 on 2021-08-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('Email', models.EmailField(max_length=254)),
                ('msg', models.CharField(max_length=200)),
            ],
        ),
    ]
