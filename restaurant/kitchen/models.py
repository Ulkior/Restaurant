from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Events(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование событий')
    price = models.FloatField(verbose_name='Цена')
    description = models.TextField(default='Подробности', verbose_name='Подробно о услугах')
    image = models.ImageField(upload_to='photos/events/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'



class Chefs(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя повара')
    chef_title = models.CharField(max_length=100, verbose_name='Звание повара')
    image = models.ImageField(upload_to='photos/chefs/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Повар'
        verbose_name_plural = 'Повара'

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория блюда')
    slug = models.SlugField(unique=True, verbose_name='Слаг', null=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Принадлежит к',
        related_name='subcategories'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория блюда'
        verbose_name_plural = 'Категории блюд'




class Kitchen(models.Model):
    title = models.CharField(max_length=155, verbose_name='Кухня')
    description = models.TextField(default='Описание кухни', verbose_name='Описание кухни')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Кухня'
        verbose_name_plural = 'Кухни'





class Meal(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название блюда')
    description = models.TextField(default='Описание', verbose_name='Описание')
    price = models.FloatField()
    slug = models.SlugField(unique=True, verbose_name='Слаг', null=True)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE, verbose_name='Категория продукта',
                                 related_name='meal')
    kitchen = models.ForeignKey(Kitchen, default=1, on_delete=models.CASCADE,
                                verbose_name='Кухня продукта')

    def __str__(self):
        return self.title

    def get_first_photo(self):
        if self.images:
            try:
                return self.images.all()[0].images.url
            except:
                return '-'
        else:
            return '-'


    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'





class Photo(models.Model):
    images = models.ImageField(upload_to='meal/')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE,
                                verbose_name='Блюдо',
                                related_name='images')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    job = models.CharField(max_length=255, default='Unemployed',
                           verbose_name='Профессия')
    avatar = models.ImageField(upload_to='photos/profiles/', null=True, blank=True,
                               verbose_name='Фото')
    phone = models.CharField(max_length=255, blank=True, null=True,
                             verbose_name='Номер телефона')
    bio = models.CharField(max_length=255, default='Инфо о себе',
                           verbose_name='Био')
    city = models.CharField(max_length=255, default='Город',
                           verbose_name='City...')
    region = models.CharField(max_length=255, default='Штат/Регион',
                           verbose_name='State/Region')
    instagram = models.CharField(max_length=255, default='@username',
                                 verbose_name='Инстаграм')
    telegram = models.CharField(max_length=255, default='@username',
                                verbose_name='Телеграм')

    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'




class Customer(models.Model):
    user = models.OneToOneField(User, models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=255, default='', verbose_name='Имя покупателя')
    last_name = models.CharField(max_length=255, default='', verbose_name='Фамилия покупателя')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'




class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_comleted = models.BooleanField(default=False)
    shipping = models.BooleanField(default=False)


    def __str__(self):
        return str(self.pk) + ' '


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    @property
    def get_cart_final_price(self):
        order_products = self.orderproduct_set.all()
        final_price = sum([product.get_total_price for product in order_products])
        return final_price


class OrderProduct(models.Model):
    product = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'


    @property
    def get_total_price(self):
        total_price = self.product.price * self.quantity
        return total_price



class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адреса доставки'




class Booking_table(models.Model):
    name = models.CharField(max_length=155, verbose_name='Имя')
    email = models.EmailField()
    phone = models.CharField(max_length=16, verbose_name='Номер телефона')
    data = models.CharField(max_length=10, verbose_name='Забронировать на дату...')
    time = models.TimeField(verbose_name='На какое время')
    people_quantity = models.IntegerField(verbose_name='Количество людей')
    message = models.TextField()
    booking_time = models.DateTimeField(auto_now_add=True, verbose_name='Время отправки сообщения')
    checked_booking = models.BooleanField(default=False, verbose_name='Проверка брони')




