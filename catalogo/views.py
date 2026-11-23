from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Jogo, Desenvolvedora, Plataforma


def lista_jogos(request):
    # 1. Lê os parâmetros enviados por GET
    busca = request.GET.get('busca', '').strip()
    desenvolvedora_sel = request.GET.get('desenvolvedora', '')
    plataforma_sel = request.GET.get('plataforma', '')

    # 2. Consulta base (select_related evita consultas extras por jogo)
    jogos = Jogo.objects.select_related('desenvolvedora', 'plataforma')

    # 3. Aplica pesquisa e filtros ANTES da paginação
    if busca:
        jogos = jogos.filter(nome__icontains=busca)
    if desenvolvedora_sel.isdigit():
        jogos = jogos.filter(desenvolvedora_id=desenvolvedora_sel)
    if plataforma_sel.isdigit():
        jogos = jogos.filter(plataforma_id=plataforma_sel)

    # 4. Paginação: 5 registros por página
    paginator = Paginator(jogos, 5)
    page_obj = paginator.get_page(request.GET.get('page'))

    # 5. Query string sem o "page", para preservar os filtros nos links
    params = request.GET.copy()
    params.pop('page', None)
    query_string = params.urlencode()

    context = {
        'page_obj': page_obj,
        'desenvolvedoras': Desenvolvedora.objects.all(),
        'plataformas': Plataforma.objects.all(),
        'busca': busca,
        'desenvolvedora_sel': desenvolvedora_sel,
        'plataforma_sel': plataforma_sel,
        'query_string': query_string,
    }
    return render(request, 'catalogo/lista_jogos.html', context)