from django import forms
from .models import Post


#유저들한테 입력받을 필터만 작성


class PostForm(forms.ModelForm):
    # title = forms.CharField(validators=[min_length_3_validator])
    # content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['title', 'content', 'user_agent']
        widgets = {
            'user_agent': forms.HiddenInput,
        }

    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post
