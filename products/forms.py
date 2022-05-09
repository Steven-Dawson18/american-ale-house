"""Products Forms"""
from django import forms
from django.core.exceptions import ValidationError
from .widgets import CustomClearableFileInput
from .models import Product, Category, ReviewRating


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']

    def clean_rating(self):
        data = self.cleaned_data['rating']
        if data < 1:
            raise ValidationError(('Please enter a rating between 1 and 5'))

        if data > 5:
            raise ValidationError(('Please enter a rating between 1 and 5'))

        return data
