# Generated by Django 4.2.2 on 2023-09-26 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0011_alter_ticket_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['created_on', 'solved']},
        ),
    ]
