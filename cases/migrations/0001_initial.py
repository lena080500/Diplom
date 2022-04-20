# Generated by Django 4.0.4 on 2022-04-19 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Case_Name', models.CharField(max_length=50, verbose_name='Название кейса')),
                ('Case_Comment', models.TextField(verbose_name='Коментарий')),
                ('Case_Title', models.TextField(verbose_name='Наименование;ИНН')),
                ('Case_Location', models.TextField(verbose_name='Год основания, месторасположения')),
                ('Case_Type_of_activity', models.TextField(verbose_name='Основные виды деятельности')),
                ('Case_Production', models.TextField(verbose_name='Выпускаемая продукция')),
                ('Case_Date', models.DateField(verbose_name='Дата создания кейса')),
            ],
            options={
                'verbose_name': 'Кейс',
                'verbose_name_plural': 'Кейсы',
            },
        ),
        migrations.CreateModel(
            name='GroupStud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, verbose_name='Название группы')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Студенты')),
            ],
            options={
                'verbose_name': 'Группа студентов',
                'verbose_name_plural': 'Группы студентов',
            },
        ),
        migrations.CreateModel(
            name='CaseSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Section_Name', models.CharField(max_length=200, verbose_name='Название раздела')),
                ('Section_Comment', models.TextField(verbose_name='Коментарий')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case.case')),
            ],
            options={
                'verbose_name': 'Раздел кейса',
                'verbose_name_plural': 'Разделы кейсов',
            },
        ),
        migrations.CreateModel(
            name='CaseParametr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Param_Name', models.CharField(max_length=200, verbose_name='Название параметра')),
                ('Param_Comment', models.TextField(verbose_name='Коментарий')),
                ('Name_Variable', models.CharField(blank=True, max_length=20, null=True, verbose_name='Имя переменной')),
                ('Formula', models.TextField(blank=True, null=True, verbose_name='Формула для вычисления этого параметра')),
                ('Param_Period', models.DateField(blank=True, verbose_name='Период сбора данных')),
                ('Param_Value', models.FloatField(null=True, verbose_name='Значение параметра')),
                ('case_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case.casesection')),
            ],
            options={
                'verbose_name': 'Параметр кейса',
                'verbose_name_plural': 'Параметры кейсов',
            },
        ),
    ]
