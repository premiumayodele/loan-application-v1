from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import pgettext, ugettext, ugettext_lazy as _
from . models import CustomerProfile

User = get_user_model()

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'What is your email address?'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'What is your password?'}))

    def __int__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Invalid Email or Password!')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password!')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please provide any username'}))
    # username = forms.CharField(widget=forms.HiddenInput())
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'What is your email'}))    
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Choose a password'}))
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your chosen password'}))
    
    class Meta:
        model = User
        fields = ('email', 'username', 'password1')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user

MARITAL_STATUS = (
    ('', 'Select Marital Status'),
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Separated', 'Separated'),
    ('Divorced', 'Divorced'),
)

EMPLOYMENT = (
    ('', 'Select Employment Status'),
    ('FTE', 'Full Time Employed'),
    ('SE', 'Self Employed'),
    ('S', 'Student'),
    ('P', 'Pension'),
    ('U', 'Unemployed'),
)

GENDER = (
    ('', 'Select Gender'),
    ('female', 'Female'),
    ('male', 'Male'),
)


class CompleteProfile(forms.ModelForm):
    first_name = forms.CharField(max_length=30,required=True, widget=forms.TextInput(attrs={'placeholder': 'What is your first name?', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'What is your last name?', 'class':'form-control' }))
    mobile = forms.CharField(max_length=14, required=True, widget=forms.TextInput(attrs={'placeholder':'What is your mobile number? (eg 234812345678', 'class': 'form-control', 'type': 'number'}))
    bvn = forms.CharField(label=_('BVN'),max_length=11, required=True, widget=forms.TextInput(attrs={'placeholder':'What is your BVN', 'class': 'form-control', 'type': 'number'}))
    dob = forms.DateField(label=_('Date of Birth'), required=True, widget=forms.DateTimeInput(attrs={'placeholder':'What is your Date of Birth', 'class': 'form-control', 'type': 'date'}))
    gender = forms.ChoiceField(label=_('Marital Status'), choices=GENDER, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    marital_status = forms.ChoiceField(label=_('Marital Status'), choices=MARITAL_STATUS, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    employment = forms.ChoiceField(label=_('Employment Status'), choices=EMPLOYMENT, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    address = forms.CharField(label=_('Contact Address'), widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What is your address?'}))
    country = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Which country are you from?', 'class':'form-control' }))
    town = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Which town are you from?', 'class':'form-control' }))
    # status = models.BooleanField(default=True)
    # created_on = models.DateTimeField(auto_now_add=True)
    # last_login_date = models.DateTimeField(auto_now=True)

    # role = forms.ModelChoiceField(label=_('Role'), queryset=Role.objects.filter(pk=3), required=True, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomerProfile
        fields = ('first_name', 'last_name', 'mobile', 'bvn', 'dob', 'marital_status', 'address', 'country', 'town')