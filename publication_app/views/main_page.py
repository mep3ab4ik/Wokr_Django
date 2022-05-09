from django.shortcuts import render


def main_page(request):
    """Функция главной страницы"""
    return render(request, 'main_page.html')