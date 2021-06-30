# Generated by Django 3.2.3 on 2021-06-30 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoyalPages', '0003_aboutus'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerys',
            name='image',
            field=models.ImageField(default='RoyalSite/images/gallery/x.png', upload_to='RoyalSite/images/gallery'),
        ),
        migrations.AddField(
            model_name='gallerys',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
