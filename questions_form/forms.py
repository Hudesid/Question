from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('name', 'email', 'question')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a email'
            }),
            'question': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter questions'
            }),

        }