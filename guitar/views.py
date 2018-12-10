from timeit import Timer

from django.shortcuts import render

from guitar.models import Guitarra


def _gerar_relatorio():
    azul_amarelo = Guitarra.objects.filter(configuracao__cor__in=['azul', 'amarelo']).select_related('configuracao').values_list('id', flat=True)
    azul_amarelo_count = len(azul_amarelo)
    seis_cordas = Guitarra.objects.filter(configuracao__cordas=6).select_related('configuracao').values_list('id', flat=True)
    seis_cordas_count = len(seis_cordas)
    prs = Guitarra.objects.filter(configuracao__modelo__marca__nome='PRS').select_related('configuracao__modelo__marca').values_list('id', flat=True)
    prs_count = len(prs)
    ada = Guitarra.objects.filter(dono='Ada').values_list('id', flat=True)
    ada_count = len(ada)

    todas = (
        Guitarra
        .objects
        .filter(id__in=azul_amarelo)
        .filter(id__in=seis_cordas)
        .filter(id__in=prs)
        .filter(id__in=ada)
    ).count()

    return {
        'azul_amarelo': azul_amarelo_count,
        'seis_cordas': seis_cordas_count,
        'prs': prs_count,
        'ada': ada_count,
        'todas_as_condicoes': todas,
    }


def relatorio(request):
    """
    quantas guitarras azul ou amarelo?
    quantas guitarras de 6 cordas?
    quantas guitarras PRS?
    quantas guitarras de Ada?
    quantas guitarrs de Ada, PRS, 6 cordas, azul ou amarelo?
    """

    timer = Timer(_gerar_relatorio)
    tempo = timer.timeit(number=100)

    data = _gerar_relatorio()
    data['tempo'] = tempo

    return render(request, 'relatorio.html', data)
