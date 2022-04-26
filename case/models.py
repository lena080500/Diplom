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
    Param_Comment = models.TextField('Комментарий', blank=True)
    #сокращенное название переменной
    Name_Variable = models.CharField('Имя переменной', max_length=5)
    Formula = models.TextField('Формула для вычисления этого параметра', blank=True)
    Param_Period = models.DateField('Период сбора данных')
    Param_Value = models.FloatField('Значение параметра', blank=True, null=True, default=None)

#поиск значения по имени переменной
    def getValue(name):
        object = CaseParametr.objects.all()
        for o in object:
            if name == o.Name_Variable:
                return o.Param_Value
        return None

#Замена имён переменных на их значения
    def newFormula(self):
        formula = self.Formula
        if formula == "":
            return
        newformula = ""
        param = ""
        value = 0
        for i, val in enumerate(formula, start=1):
            if (val != '(') and (val != ')') and (val != '*') and (val != '/') and (val != '+') and (val != '-') and (val != ' '):
                param = param + val
            else:
                if ((val == '+') or (val == '-') or (val == '*') or (val == '/') or (val == ')') or (val == '(')) and (param != ""):
                    value = CaseParametr.getValue(param)
                    if value == None:
                        newformula = newformula + param
                    else:
                        newformula = newformula + f'{value}'
                    param = ""
                newformula = newformula + val
        value = CaseParametr.getValue(param)
        if value == None:
            newformula = newformula + param
        else:
            newformula = newformula + f'{value}'
        value = CaseParametr.Сalculator(newformula)
        self.Param_Value = value

#Считает только если в формуле одни числа
    def Сalculator(formula):
        return eval(formula)

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