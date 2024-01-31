from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
from .utils import *

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя:",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'id': 'Input1',
                                   'placeholder': 'Username ...'
                               }))
    password = forms.CharField(label="Пароль:",
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'id': 'Input2',
                                   'placeholder': 'Password ...'
                               }))






class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя:",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username ...'
                               }))
    first_name = forms.CharField(label="Ваше имя:",
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Your name ...'
                                 }))
    last_name = forms.CharField(label="Ваша фамилия:",
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Your lastname ...'
                                }))

    email = forms.EmailField(label="Ваша почта:",
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Your email ...'
                             }))

    password1 = forms.CharField(label="Придумайте пароль:",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Password ...'
                                }))
    password2 = forms.CharField(label="Подтвердите пароль:",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Password ...'
                                }))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )



class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(label="Имя пользователя:",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username ...'
                               }))
    first_name = forms.CharField(label="Ваше имя:",
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Your name ...'
                                 }))
    last_name = forms.CharField(label="Ваша фамилия:",
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Your lastname ...'
                                }))
    email = forms.EmailField(label="Ваша почта:",
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Your email ...'
                             }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'job', 'city', 'region', 'bio',
                  'instagram', 'telegram', 'phone')

        widgets = {
            'avatar': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'job': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Профессия ...'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес ...'
            }),
            'region': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес ...'
            }),
            'bio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Коротко о себе ...'
            }),
            'instagram': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Инстаграм ...'
            }),
            'telegram': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телеграм ...'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона ...'
            })
        }



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'first_name',
            'last_name'
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя...'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша фамилия...'
            })
        }


class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ('address', 'city', 'phone')
        widgets = {
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес...'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город...'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона...'
            })
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking_table
        fields = ('name','email','phone',
                  'data','time','people_quantity',
                  'message')
        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона...'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя...'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта...'
            }),
            'data': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата...'
            }),
            'time': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время...'
            }),
            'people_quantity': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кол-во гостей...'
            }),
            'message': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дополнительные пожелания..'
            }),
        }





