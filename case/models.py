from django.contrib.auth.models import User
from django.db import models


#Класс для обзорной информации предприятия/региона
class Case(models.Model):
    Case_Name = models.CharField('Название кейса', max_length=50)
    Case_Comment = models.TextField('Коментарий')
    Case_Title = models.TextField('Наименование;ИНН')
    Case_Location = models.TextField('Год основания, месторасположения')
    Case_Type_of_activity = models.TextField('Основные виды деятельности')
    Case_Production = models.TextField('Выпускаемая продукция')
    Case_Date = models.DateField('Дата создания кейса')

    def __str__(self):
        return self.Case_Name

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'


class CaseSection(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    Section_Name = models.CharField('Название раздела', max_length=200)
    Section_Comment = models.TextField('Комментарий')

    def __str__(self):
        return self.Section_Name

    class Meta:
        verbose_name = 'Раздел кейса'
        verbose_name_plural = 'Разделы кейсов'


class CaseParametr(models.Model):
    case_section = models.ForeignKey(CaseSection, on_delete=models.CASCADE)
    Param_Name = models.CharField('Название параметра', max_length=200)
    Param_Comment = models.TextField('Комментарий')
    #сокращенное название переменной
    Name_Variable = models.CharField('Имя переменной', max_length=20, blank=True, null=True)
    Formula = models.TextField('Формула для вычисления этого параметра', blank=True, null=True)
    Param_Period = models.DateField('Период сбора данных', blank=True)
    Param_Value = models.FloatField('Значение параметра', null=True)

    def __str__(self):
        return self.Param_Name

    class Meta:
        verbose_name = 'Параметр кейса'
        verbose_name_plural = 'Параметры кейсов'


class GroupStud(models.Model):
    Name = models.CharField(max_length=30, verbose_name='Название группы')
    users = models.ManyToManyField(User, verbose_name='Студенты')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Группа студентов'
        verbose_name_plural = 'Группы студентов'