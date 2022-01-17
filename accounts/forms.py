from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class PasswordChangeForms(PasswordChangeForm):

    def _init_(self, *args, **kwargs):
        super(PasswordChangeForms, self)._init_(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'
        self.fields['old_password'].label = ''
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password1'].label = ''
        self.fields[
            'new_password1'].help_text = '<ul class ="form-text text-muted small"><li>Your password can\'t be too ' \
                                         'similar to your other personal information.</li><li>Your password must ' \
                                         'contain at least 8 characters.</li><li>Your password can\'t be a commonly ' \
                                         'used password.</li><li>Your password can\'t be entirely numeric.</li></ul> '

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['new_password2'].label = ''


class EditUserForm(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)

    def _init_(self, args, *kwargs):
        super(EditUserForm, self)._init_(args, *kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'user name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class ="form-text text-muted"><small>Required. 150 characters or fewer. ' \
                                    'Letters, digits and @/./+/-/_ only.</small></span> '

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'first name'
        self.fields['first_name'].label = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'last name'
        self.fields['last_name'].label = ''

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'email address'
        self.fields['email'].label = ''


class SignUpForm(UserCreationForm):

    def __int__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widgets.attrs.update(
            {
                'placeholder': 'Enter your first name',

            }
        )
        self.fields['email'].widgets.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )

        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

