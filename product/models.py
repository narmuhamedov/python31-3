from django.db import models

class Customer(models.Model):
    name = models.CharField('Имя заказчика', max_length=100)
    phone = models.CharField('Номер телефона', max_length=100)

    class Meta:
        verbose_name = 'заказчика'
        verbose_name_plural = 'заказчики'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name_tag = models.CharField('Укажите хэштег', max_length=100)

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name_tag

class Product(models.Model):
    title = models.CharField('Название продукта', max_length=100)
    image = models.ImageField('Фото продукта', upload_to='product/')
    price = models.PositiveIntegerField('Цена')
    tag = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


    def __str__(self):
        return self.title

class StatusOrder(models.Model):
    STATUS = (
        ('Ожидание', 'Ожидание'),
        ('Выехал', 'Выехал'),
        ('Доставлен', 'Доставлен'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS)

    class Meta:
        verbose_name = 'статус доставки'
        verbose_name_plural = 'статусы доставок'

    def __str__(self):
        return self.status

