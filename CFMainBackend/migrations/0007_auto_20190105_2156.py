# Generated by Django 2.1.5 on 2019-01-05 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CFMainBackend', '0006_actorvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actorvideo',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='CFMainBackend.Actor'),
        ),
    ]
