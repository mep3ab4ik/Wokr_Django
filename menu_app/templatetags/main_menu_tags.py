from django import template
from django.urls import reverse_lazy, reverse

from ..models import Menu

register = template.Library()


# Путь к нашему "html-тэгу"
@register.inclusion_tag('menu_app/menu.html')
def main_menu():
    menu = Menu.objects.get(menu_label='main_menu')
    return {'menu': menu.links.all()}


@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def profile_menu(context):
    if context.request.user.is_authenticated:
        menu = [
            {
                'title': f'Добро пожаловать, {context.request.user.username}!',
                'url': reverse_lazy('your_account'),
            },
            {
                'title': 'Выйти',
                'url': reverse_lazy('logout'),
            },
        ]
        if context.request.user.is_superuser or context.request.user.is_staff:
            menu.insert(0, {'title': 'Админка', 'url': '/admin/'})
    else:
        menu = [
            {
                'title': 'Авторизация',
                'url': reverse_lazy('login'),
            },
            {
                'title': 'Регистрация',
                'url': reverse_lazy('register'),
            },
        ]
    return {'menu': menu}
