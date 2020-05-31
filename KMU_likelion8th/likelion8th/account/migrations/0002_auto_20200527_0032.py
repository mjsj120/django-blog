# Generated by Django 3.0.6 on 2020-05-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customusermodel',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', '남자'), ('F', '여자')], max_length=2, null=True),
        ),
    ]
