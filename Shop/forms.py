from django import forms
class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100)
    required_css_class = "uk-search-input"
