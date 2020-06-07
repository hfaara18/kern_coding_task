from django import forms


class StringForm(forms.Form):
    input_string = forms.CharField(widget=forms.TextInput(attrs={'id':'string-form', 'class': 'form-control', 'autocomplete':'off'}))


class DNATemplateForm(forms.Form):
    input_dna_templates = forms.CharField(widget=forms.TextInput(attrs={'id':'dna-template-form', 'class': 'form-control', 'autocomplete':'off'}))
