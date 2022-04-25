from .models import Case
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = ['Case_Name', 'Case_Comment', 'Case_Title', 'Case_Location', 'Case_Type_of_activity', 'Case_Production', 'Case_Date']
        widgets = {
            "Case_Name": TextInput(attrs={
                'placeholder':'Название кейса'
            }),
            "Case_Comment": Textarea(attrs={
                'placeholder': 'Коментарий'
            }),
            "Case_Title": Textarea(attrs={
                'placeholder': 'Наименование, ИНН'
            }),
            "Case_Location": Textarea(attrs={
                'placeholder': 'Год основания, месторасположения'
            }),
            "Case_Type_of_activity": Textarea(attrs={
                'placeholder': 'Основные виды деятельности'
            }),
            "Case_Production": Textarea(attrs={
                'placeholder': 'Выпускаемая продукция'
            }),
            "Case_Date": DateTimeInput(attrs={
                'placeholder': 'Дата создания кейса'
            }),
        }