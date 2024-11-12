from django import forms

# models
from .models import Suscribers, Contact

class SuscribersForm(forms.ModelForm):
    """Form definition for Suscribers."""

    class Meta:
        """Meta definition for Suscribersform."""

        model = Suscribers
        fields = (
            'email',
        )
        # personaliza la cajita de ingreso
        widgets = {
            'email': forms.EmailInput (
                attrs={
                'placeholder': 'digite su email',
                'class': 'input-email'
                }
            ),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')

    

