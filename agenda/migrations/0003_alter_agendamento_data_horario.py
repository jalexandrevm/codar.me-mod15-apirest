# Generated by Django 4.0.3 on 2022-03-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_alter_agendamento_nome_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='data_horario',
            field=models.DateTimeField(),
        ),
    ]
