import time
from django.http import HttpResponse, JsonResponse # type: ignore
from django.shortcuts import render, redirect # type: ignore
 
 
def homepage(request):
    return render(request, "homepage.html") 

def formulario(request):
    return render(request, 'formulario.html')

def sucesso(request):
    return render(request, "sucesso.html") 

def gerar_relatorio(request):
    if request.method == "POST":
        nome = request.POST.get("user-name")
        email = request.POST.get("user-email")
        codigo_imovel = request.POST.get("texto")
        
        # Lógica para processar os dados
        time.sleep(3)
        
        
        # Exemplo: salvar no banco de dados, gerar arquivo, etc.
        print(f"Nome: {nome}, Email: {email}, Código: {codigo_imovel}")
        # Redirecionar para a página de sucesso
        return redirect("sucesso")
    else:
        return JsonResponse({"error": "Método não permitido"}, status=405)


