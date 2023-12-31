# Generated by Django 4.2.5 on 2023-09-10 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_api', '0002_imagemodel_address_imagemodel_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='voice_text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='voice_recording',
            field=models.FileField(default='', upload_to='voices/'),
        ),
    ]
