# Generated by Django 3.2.3 on 2021-09-24 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoyalPages', '0010_aboutus_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='background',
            field=models.ImageField(default='RoyalSite/static/RoyalSite/images/gallery/x.png', upload_to='RoyalSite/static/RoyalSite/css/'),
        ),
    ]
