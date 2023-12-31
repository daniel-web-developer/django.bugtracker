# Generated by Django 4.2.2 on 2023-07-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_alter_ticket_description_alter_ticket_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='edited_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='public',
            field=models.BooleanField(choices=[(True, 'Public'), (False, 'Private')], default=False),
        ),
    ]
