# Generated by Django 3.2.3 on 2021-06-29 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoyalPages', '0002_auto_20210625_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
    ]