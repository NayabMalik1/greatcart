
from django import forms
from .models import ReviewRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']
    
    rating = forms.IntegerField(widget=forms.HiddenInput, initial=5)

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs['placeholder'] = 'Write a subject'
        self.fields['review'].widget.attrs['placeholder'] = 'Write your review here'
        self.fields['rating'].widget.attrs['style'] = 'display: none;'  # Hide the rating field