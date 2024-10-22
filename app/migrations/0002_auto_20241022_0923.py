# app/migrations/0002_auto_add_data.py

from django.db import migrations

def add_initial_data(apps, schema_editor):
    Posto = apps.get_model('app', 'Posto')
    Medico = apps.get_model('app', 'Medico')
    Area = apps.get_model('app', 'Area')

    # Adiciona áreas para os médicos
    area_clinica = Area.objects.create(nome='Clínica Geral')
    area_pediatria = Area.objects.create(nome='Pediatria')
    area_cardiologia = Area.objects.create(nome='Cardiologia')

    # Adiciona postos de saúde
    posto_1 = Posto.objects.create(nome='Posto de Saúde Central', endereco='Rua A, 123', telefone='1234-5678')
    posto_2 = Posto.objects.create(nome='Posto de Saúde Norte', endereco='Rua B, 456', telefone='8765-4321')

    # Adiciona médicos
    Medico.objects.create(nome='Dr. João Silva', area=area_clinica)
    Medico.objects.create(nome='Dra. Maria Oliveira', area=area_pediatria)
    Medico.objects.create(nome='Dr. Carlos Souza', area=area_cardiologia)

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),  # Altere para o nome da sua migração anterior
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
