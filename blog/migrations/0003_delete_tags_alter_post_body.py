# Generated by Django 4.0.6 on 2022-08-04 00:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]