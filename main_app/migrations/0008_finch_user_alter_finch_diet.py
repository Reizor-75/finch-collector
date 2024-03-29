# Generated by Django 4.2.10 on 2024-03-04 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0007_finch_weapons'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='finch',
            name='diet',
            field=models.CharField(choices=[('I', 'Insects'), ('C', 'Cactus'), ('S', 'Seeds'), ('T', 'Trash')], default='I', max_length=100),
        ),
    ]
