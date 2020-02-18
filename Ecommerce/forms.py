from django import forms 

class ReviewForm(forms.Form): 
    Review = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
