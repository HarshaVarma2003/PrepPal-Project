# Generated by Django 5.0.6 on 2024-05-26 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_previousyearquestion_document_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='previousyearquestion',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='previousyearquestion',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='previous_year_questions/'),
        ),
        migrations.AlterField(
            model_name='studymaterial',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_materials', to='blog.subject'),
        ),
    ]