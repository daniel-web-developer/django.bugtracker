# Generated by Django 4.2.2 on 2023-07-12 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.SmallIntegerField(choices=[(0, 'Low priority'), (1, 'Medium priority'), (2, 'High priority')], default='0'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='issues.project'),
        ),
    ]
