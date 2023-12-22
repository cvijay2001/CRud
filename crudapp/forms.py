from django import forms
from .models import Employee

# common attributes for all below fields except eprofilephoto
common_attrs = {
    'class': 'form-control',
}

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['eid', 'ename', 'eemail', 'econtact', 'eprofilephoto']

    # Define fields with common attributes and specific attributes
    eid = forms.IntegerField(
        min_value=1,
        max_value=99999,
        required=True,
        widget=forms.NumberInput(attrs={**common_attrs, 'placeholder': 'Enter Employee ID'}),
        label='Employee ID'
    )

    ename = forms.CharField(
        min_length=3,
        max_length=55,
        required=True,
        widget=forms.TextInput(attrs={**common_attrs, 'placeholder': 'Enter Employee Name'}),
        label='Employee Name'
    )

    eemail = forms.EmailField(
        widget=forms.EmailInput(attrs={**common_attrs, 'placeholder': 'Enter Employee Email'}),
        label='Employee Email'
    )

    econtact = forms.CharField(
        widget=forms.TextInput(attrs={**common_attrs, 'placeholder': 'Enter Employee Contact'}),
        label='Employee Contact'
    )


    eprofilephoto = forms.FileField(
        widget=forms.ClearableFileInput(attrs={**common_attrs,'accept':'image/*','id':'eprofilephoto', 'onchange':"validateForm()", 'placeholder': 'Select Employee Profile Photo'}),
        label='Employee Profile Photo'
    )

    def clean_econtact(self):
        econtact = self.cleaned_data['econtact']
        if len(str(econtact)) != 10 or not str(econtact).isdigit():
            raise forms.ValidationError("Please enter a 10-digit valid contact number.")
        return econtact

    def clean_ename(self):
        ename = self.cleaned_data['ename']
        if not ename.replace(" ", "").isalpha():
            raise forms.ValidationError("Please enter a valid name containing only alphabetic characters.")
        return ename


    def clean_eid(self):
        eid = self.cleaned_data['eid']
        if not str(eid).isalnum():
            raise forms.ValidationError("Please enter a valid alphanumeric employee ID.")
        return eid

