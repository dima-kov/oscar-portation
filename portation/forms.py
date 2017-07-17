from django import forms
from django.utils.translation import ugettext_lazy as _

from oscar.apps.catalogue.models import ProductClass


class ImportForm(forms.Form):

    file = forms.FileField(
        label=_('File with backup'),
    )


class ExportForm(forms.Form):

    product_class = forms.ModelChoiceField(
        queryset=None,
        label=_('Product class'),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ExportForm, self).__init__(*args, **kwargs)
        self.fields['product_class'].queryset = ProductClass.objects.all()
