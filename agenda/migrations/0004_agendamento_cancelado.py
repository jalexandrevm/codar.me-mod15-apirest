# Generated by Django 4.0.3 on 2022-03-28 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_alter_agendamento_data_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='cancelado',
            field=models.BooleanField(default=False),
        ),
    ]
