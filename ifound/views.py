from django.shortcuts import render, redirect

def index(request):
    query = request.GET.get('q')
    
    itens = [
        {'nome': 'Nome do objeto', 'imagem': None},
        {'nome': 'Nome do objeto', 'imagem': None},
        {'nome': 'Nome do objeto', 'imagem': None},
    ]

    if query:
        itens = [item for item in itens if query.lower() in item['nome'].lower()]

    return render(request, 'index.html', {'itens': itens})