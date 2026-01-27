from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, SellerProfile
class ClientRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'CLIENT'
        if commit:
            user.save()
        return user
class SellerRegisterForm(UserCreationForm):
    seller_type = forms.ChoiceField(
        choices=SellerProfile.SELLER_TYPES
    )
    phone = forms.CharField(max_length=20)
    description = forms.CharField(
        widget=forms.Textarea,
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'SELLER'

        if commit:
            user.save()
            SellerProfile.objects.create(
                user=user,
                seller_type=self.cleaned_data['seller_type'],
                phone=self.cleaned_data['phone'],
                description=self.cleaned_data['description']
            )
        return user
