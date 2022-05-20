from django import template
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
                'url': '/your_account',
            },
            {
                'title': 'Выйти',
                'url': '/logout',
            },
        ]
    else:
        menu = [
            {
                'title': 'Авторизация',
                'url': '/login',
            },
            {
                'title': 'Регистрация',
                'url': '/register',
            },
        ]
    return {'menu': menu}