# Generated by Django 4.0a1 on 2021-11-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0014_remove_courese_selected_ai_scoure_one_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_score',
            name='evaluate',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
