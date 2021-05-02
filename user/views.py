from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib import messages



# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            #username = form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            # messages.success(
            #    request, 'تهانينا {} لقد تمت عملية التسجيل بنجاح.'.format(username))
            messages.success(
                request, f'Поздравляем Вас.. Вы успешно зарегистрировалась на нашем сайте.')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {
        'title': 'Регистрация',
        'form': form,
    })