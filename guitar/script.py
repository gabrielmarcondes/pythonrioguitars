import random

from guitar.models import Guitarra, Configuracao, Modelo, Marca

MARCAS = [
    'Les Paul',
    'Fender',
    'Tagima',
    'Seizi',
    'PRS',
    'Ibanez',
    'Condor',
]

DONOS = [
    'Ada',
    'Alan',
    'Margaret',
    'Gabriel',
    'Dijkstra',
]

CORES = [
    'vermelho',
    'amarelo',
    'azul',
    'preto',
    'branco',
    'verde',
    'prata',
    'transparente',
    'madeira',
]

CORDAS = [6, 7]

ANOS = list(range(1958, 2019))

novas_marcas = []
for marca in MARCAS:
    novas_marcas.append(Marca(nome=marca))
Marca.objects.bulk_create(novas_marcas)


for marca in Marca.objects.all():
    novos_modelos = []
    for i in range(10):
        nome = 'Modelo {}'.format(i)
        novos_modelos.append(
            Modelo(nome=nome, marca=marca)
        )
    Modelo.objects.bulk_create(novos_modelos)


for modelo in Modelo.objects.all():
    novas_configs = []
    for i in range(10):
        novas_configs.append(
            Configuracao(
                modelo=modelo,
                cor=random.choice(CORES),
                cordas=random.choice(CORDAS),
                ano=random.choice(ANOS),
            )
        )
    Configuracao.objects.bulk_create(novas_configs)


todas_configuracoes = Configuracao.objects.all().values_list('id', flat=True)

for dono in DONOS:
    novas_guitarras = []
    for i in range(1000):
        novas_guitarras.append(
            Guitarra(dono=dono, configuracao_id=random.choice(todas_configuracoes))
        )
    Guitarra.objects.bulk_create(novas_guitarras)
