from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile, Event, EventMember



class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    fields = ('title','description','start_date','end_date','start_time','end_time')
    widgets = {
      'start_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%dT%H:%M'),
      'end_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%dT%H:%M'),
      #'start_time': forms.DateInput(attrs={'type': 'time'}, format='%Y-%m-%dT%H:%M'),
      #'end_time': forms.DateInput(attrs={'type': 'time'}, format='%Y-%m-%dT%H:%M'),
    }
    exclude = ['user']
'''
  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    """A test!"""
    print("Test.")
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%H:%M',)
    self.fields['end_time'].input_formats = ('%H:%M',)'''




class UserProfileForm(forms.ModelForm):
    location     = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={"class": "form-control",'placeholder':'Location'}))
    team         = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':'Team'}))
    group  		 = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':'Group'}))
    phonenumber  = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':'Phone Number'}))
    
    class Meta:
    	model = UserProfile
    	fields = ('location','team','group','phonenumber')


class HardWareForm(forms.Form):
	#label for="asset_number" class="col-sm col-form-label"
    AssetNo          = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Asset Number'}))
    Owner            = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Asset Owner'}))
    AssetTypeModel   = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Asset Type/Model'}))
    Group            = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Group'}))
    TeamName         = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Team'}))
    ProductLine      = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Product line'}))
    Remark           = forms.CharField(label="", max_length=400, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Remark'}))

class EditProfileForm(UserChangeForm):
	password = forms.CharField(label="",  widget=forms.TextInput(attrs={'type':'hidden'}))
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password',)

class PasswordReset(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder" : "Email","class": "form-control"}))

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Username","class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder" : "Password","class": "form-control"}))

class SignUpForm(UserCreationForm):
	#forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Location'}))
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Username","class": "col-sm col-form-label"}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder" : "Email","class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder" : "Password","class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder" : "Password check","class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name','password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Windows NT ID</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'