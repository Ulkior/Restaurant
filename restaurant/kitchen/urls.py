from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('menu/', menu, name='menu' ),
    path('category/<slug:slug>/', all_meals_page, name='meals_page'),
    path('subcategory/<slug:slug>/', sub_cat_page, name='sub_meals_page'),

    path('login/', login_user, name='login_user'),
    path('registration/', registration, name='registration'),
    path('logout/', logout_user, name='logout_user'),
    path('profile_page<int:user_id>/', profile_page, name='profile_page'),
    path('change_profile<int:user_id>/', change_profile, name='change_profile'),

    path('cart/', cart, name='cart'),
    path('to_cart/<int:product_id>/<str:action>/', to_cart, name='to_cart'),
    path('clear_cart/', clear_cart, name='clear_cart'),
    path('checkout/', checkout, name='checkout'),
    path('book_table/', book_a_table, name='book_table'),
]
