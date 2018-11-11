from django import forms
from apps.product_docs.models import *


class AddInstallDocForm(forms.ModelForm):
    class Meta:
        model = InstallDoc
        exclude = ['doc_author', 'add_time']
