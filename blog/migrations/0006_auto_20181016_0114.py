# Generated by Django 2.0.5 on 2018-10-16 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_rec_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rec_value',
            field=models.IntegerField(default=2),
        ),
    ]
