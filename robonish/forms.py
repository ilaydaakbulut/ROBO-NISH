from django import forms
from .models import Register,Robot

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('name', 'surname','robot_name','category','email','phone','school_name',)
        def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs = {'class': 'form-control'}   