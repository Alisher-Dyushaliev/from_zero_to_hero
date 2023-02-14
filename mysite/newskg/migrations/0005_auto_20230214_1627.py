# Generated by Django 3.0.2 on 2023-02-14 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newskg', '0004_auto_20230119_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='newskg',
            name='browsing',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newskg',
            name='content',
            field=models.TextField(verbose_name='Framework'),
        ),
        migrations.AlterField(
            model_name='newskg',
            name='purpose',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='get_langs', to='newskg.Purpose'),
        ),
    ]
