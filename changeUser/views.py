from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import templates
from .forms import UserCreationForm, RecordCreationForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request) -> HttpResponse:
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            if form.check_password():
                form.save()
                return redirect('home')
        else: form.add_error(None, 'Эээ бля форму заполнил нормально, моросить перестал баляя')
    else:
        form = UserCreationForm
    return render(request, 'reg.html', {'form': form})


def log_in(request) -> HttpResponse:
    user_name = input('Логин: ')
    pass_word = input('Пароль: ')
    user = authenticate(request, username=user_name, password=pass_word)
    if user is None:
        print('Нет такого пользователя')
        return HttpResponse(request, '<h1>Неправильно</h1>')
    else:
        login(request, user)
        return HttpResponse(request, '<h1>Вы успешно авторизованы</h1>')
    

@login_required
def log_out(request) -> HttpResponse:
    logout(request)
    return HttpResponse(request, '<h1> Вы успешно вышли </h1>')


@login_required
def change_password(request):
    password = input('Введите новый пароль: ')
    user = request.user
    user.set_password(password)
    user.save()

    return HttpResponse(request, '<h1>Пароль успешно сменён</h1>')


@login_required
def create_record(request):
    if request.method == 'POST':
        form = RecordCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else: HttpResponse(request, 'Динаху')
    else:
        form = RecordCreationForm()
    return render(request, 'record_creation.html', {'form':form})


@login_required
def set_cookie_view(request):
    response = HttpResponse('Куки установлены')
    response.set_cookie('username', 'NIGGA')
    return response


def get_cookie_view(request):
    username = request.COOKIES.get('username')
    print(username)
    return HttpResponse(f'Username: {username}')


def delete_cookie_view(request):
    response = HttpResponse('Куки удалены!')
    response.delete_cookie('username')


def test_cookie_view(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        return HttpResponse('Работает')
    else: return HttpResponse('Не работает')