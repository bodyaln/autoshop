from django.db import models
from django.urls import reverse


class Auto(models.Model):
    CONDITION_CHOICES=[
        ('Б/У', 'Б/У'),
        ('Нове', 'Нове')
    ]
    TRANS_CHOICES =[
        ('Автомат', 'Автомат'),
        ('Механiка', "Механiка"),
        ('Варiатор', "Варiатор")
    ]
    FUEL_CHOICES = [
        ('Бензин', 'Бензин'),
        ('Дизель', "Дизель"),
        ('Газ', "Газ"),
        ('Електро','Електро')
    ]
    FIRM_CHOICES = [
        ('Audi', 'Audi'),
        ('BMW', 'BMW'),
        ('Mercedes', 'Mercedes-Benz'),
        ('Porshe', 'Porshe'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
        ('Lamborghini', 'Lamborghini'),
        ('Ferrari', 'Ferrari'),
        ('Kia', 'Kia'),
        ('Skoda', 'Skoda'),
        ('Volkswagen', 'Volkswagen')
    ]
    dict_marks = {'Audi': ["RS6", "RS5", "Q5", "Q7", "Q8", "A6"],
                  'BMW': ["3 Series", "5 Series", "7 Series", "X5", "M5", "M8"],
                  'Mercedes': ["A-Class", "B-Class", "C-Class", "E-Class", "GLE-Class"],
                  'Porshe': ["991", "Panamera", "Boxter", "Macan"],
                  'Ford': ["Mustang", "Focus"],
                  'Toyota': ["Camry", "Corolla", "Land cruiser"],
                  'Lamborghini': ["Huracan", "Urus"],
                  'Ferrari': ["812", "Diablo"],
                  'Kia': ["Rio", "Sportage", "Ceed", "K5"],
                  'Skoda': ["Superb", "Octavia A5", "Octavia A7", "Fabia"],
                  'Volkswagen': ["Golf", "Passat", "Tiguan", "Touareg"]}
    MARK_CHOICES = []
    firm = models.CharField(max_length=25,choices=FIRM_CHOICES, verbose_name="Фирма")
    mark = models.CharField(max_length=40, verbose_name="Марка")
    condition = models.CharField(max_length=40, choices=CONDITION_CHOICES, verbose_name="Стан")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URl")
    content = models.TextField(blank=True, verbose_name="Опис")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото")
    price = models.PositiveIntegerField(verbose_name="Цена")
    year = models.PositiveIntegerField(verbose_name="Год")
    distance = models.PositiveIntegerField(verbose_name="Пробег")
    power = models.PositiveIntegerField(verbose_name="Лошадок")
    transmission = models.CharField(max_length=40, choices=TRANS_CHOICES, verbose_name="Коробка")
    fuel = models.CharField(max_length=40, choices=FUEL_CHOICES, verbose_name="Паливо")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")
    shops = models.ForeignKey('Shops', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.firm} {self.mark} ({self.year})"

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Автомобiль'
        verbose_name_plural = 'Автомобiлi'
        ordering = ['id']


class Shops(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Магазин")
    photo = models.ImageField(upload_to="photos_shops/%Y/%m/%d", verbose_name="Фото")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URl")
    content = models.TextField(blank=True, verbose_name="Опис")
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shops', kwargs={'shops_slug': self.slug})

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['id']



