from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.auth.models import User


class ConsType(models.Model):
    name = models.CharField(verbose_name='Тип расходника', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Тип расходника'
        verbose_name_plural = 'Типы расходников'


class Firm(models.Model):
    name = models.CharField(verbose_name='Название фирмы', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Фирма'
        verbose_name_plural = 'Фирмы'


class StoreItem(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=255)
    firm = models.ForeignKey(Firm, verbose_name= 'Фирма', on_delete=models.CASCADE, default=None)
    type = models.ForeignKey(ConsType, verbose_name='Тип', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Расходный материал'
        verbose_name_plural = u'Расходные материалы'


class MoveItem(models.Model):
    name = models.ForeignKey(ConsType, verbose_name='Тип расходного материала', on_delete=models.CASCADE)
    type = ChainedForeignKey(
        StoreItem,
        chained_field="name",
        chained_model_field="type",
        show_all=False,
        auto_choose=True,
        sort=True,
        name=''
    )
    date_in = models.DateField(verbose_name='Дата прихода', blank=True, null=True, help_text='Указывайте дату только '
                                                                                             'тогда,  когда приходит '
                                                                                             'материал на склад')
    date_out = models.DateField(verbose_name='Дата ухода', blank=True, null=True, help_text='Указывайте дату только '
                                                                                            'тогда, материал уходит '
                                                                                            'со склада')
    count = models.IntegerField(verbose_name='Количество',
                                help_text='Ставьте "-" перед количеством для выдачи товара,\n'

                                          'оставляйте положительным для поступления на '
                                          'склад')
    tip = models.TextField(verbose_name='Заметка')
    user = models.CharField(max_length=255, verbose_name='Установил', blank=True, help_text='Указывается только при '
                                                                                           'расходе материала')

    def __str__(self):
        return self.name.name

    class Meta:
        verbose_name = u'Движение расходных материалов'
        verbose_name_plural = u'Движения расходных материалов'
