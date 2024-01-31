from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import *
from .models import *
from .utils import *


# Create your views here.


def index(request):
    chefs = Chefs.objects.all()
    events = Events.objects.all()
    context = {
        'title': 'Главная страница',
        'chefs': chefs,
        'events': events,
        'form': BookingForm()
    }

    return render(request, 'kitchen/index.html', context)


def menu(request):
    meals = Meal.objects.all()
    kitchens = Kitchen.objects.all()
    context = {
        'title': 'Меню',
        'meals': meals,
        'kitchens': kitchens
    }

    return render(request, 'kitchen/menu.html', context)


def all_meals_page(request, slug):
    category = Category.objects.get(slug=slug)
    subcategories = category.subcategories.all()
    subcategory_meals = Meal.objects.filter(category__in=subcategories)
    context = {
        'subcategory_meals': subcategory_meals,
    }

    return render(request, 'kitchen/meals_page.html', context)


def sub_cat_page(request, slug):
    subcategory = Category.objects.get(slug=slug)
    subcategory_meals = Meal.objects.filter(category=subcategory)
    context = {
        'subcategory_meals': subcategory_meals
    }

    return render(request, 'kitchen/meals_page.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login_user')
        else:
            return redirect('login_user')
    else:
        form = LoginForm()

    context = {
        'form': form,
        'title': 'Вход'
    }

    return render(request, 'kitchen/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            return redirect('login_user')
        else:
            return redirect('registration')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
        'title': 'Регистрация пользователя'
    }

    return render(request, 'kitchen/registration.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


def profile_page(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)
    context = {
        'title': 'Профиль пользователя',
        'profile': profile
    }

    return render(request, 'kitchen/profile_page.html', context)


def change_profile(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        user_form = UpdateUserForm(instance=user, data=request.POST)
        profile_form = UpdateProfileForm(instance=profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_page', user_id)
        else:
            # error message
            return redirect('change_profile', user_id)
    else:
        user_form = UpdateUserForm(instance=user)
        profile_form = UpdateProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'title': 'Изменить профиль'
    }

    return render(request, 'kitchen/change_profile.html', context)


def cart(request):
    next_page = request.META.get('HTTP_REFERER')
    cart_info = get_cart_data(request)

    context = {
        'title': 'Корзина',
        'next_page': next_page,
        'cart_total_price': cart_info['cart_total_price'],
        'order': cart_info['order'],
        'products': cart_info['products']
    }

    return render(request, 'kitchen/cart.html', context)


def to_cart(request, product_id, action):
    if request.user.is_authenticated:
        user_cart = CartForAuthenticatedUser(request, product_id, action)
        return redirect('cart')
    else:
        return redirect('login_user')


def clear_cart(request):
    user_cart = CartForAuthenticatedUser(request)
    order = user_cart.get_cart_info()['order']
    order_products = order.orderproduct_set.all()
    for order_product in order_products:
        quantity = order_product.quantity
        product = order_product.product
        order_product.delete()
        product.save()
    return redirect('cart')


def checkout(request):
    cart_info = get_cart_data(request)

    context = {
        'title': 'Оформление заказа',
        'cart_total_price': cart_info['cart_total_price'],
        'products': cart_info['products'],
        'order': cart_info['order'],
        'customer_form': CustomerForm(),
        'shipping_form': ShippingForm()
    }

    return render(request, 'kitchen/checkout.html', context)


def book_a_table(request):
    form = BookingForm(data=request.POST)
    if form.is_valid():
        form.save()
        # success message
        return render(request, 'index.html')
    else:
        # error message
        print(form.errors)
        return redirect("index")
