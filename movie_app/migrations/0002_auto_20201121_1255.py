# Generated by Django 3.1.3 on 2020-11-21 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='directory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_app.person'),
        ),
    ]
