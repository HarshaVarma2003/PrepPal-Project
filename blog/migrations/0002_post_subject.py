# Generated by Django 5.0.6 on 2024-05-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.CharField(default='No Subject', max_length=200),
            preserve_default=False,
        ),
    ]
