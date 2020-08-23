from django import forms


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
    #<input type = "text"로 랩핑됌