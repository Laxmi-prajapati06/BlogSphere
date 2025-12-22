from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Category

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Style all fields
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Choose a username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'category', 'image']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Style title field
        self.fields['title'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your post title',
            'id': 'id_title'
        })
        
        # Style excerpt field
        self.fields['excerpt'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Brief summary of your post (optional)',
            'rows': 3,
            'id': 'id_excerpt'
        })
        
        # Style content field
        self.fields['content'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Write your post content here...',
            'rows': 10,
            'id': 'id_content'
        })
        
        # Style category field - this was likely the problem!
        self.fields['category'].widget = forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_category'
        })
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].empty_label = "Select a category"
        
        # Style image field
        self.fields['image'].widget = forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'id': 'id_image'
        })
        
        # Add help texts
        self.fields['title'].help_text = 'Enter a descriptive title for your post'
        self.fields['excerpt'].help_text = 'Brief summary (max 300 characters)'
        self.fields['content'].help_text = 'Write your main content here'