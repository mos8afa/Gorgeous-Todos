from django.forms import ModelForm ,TextInput
from .models import ToDo

class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['name']
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'editTodoInput',   
                    'placeholder': 'Enter todo text...'
                }
            )
        }