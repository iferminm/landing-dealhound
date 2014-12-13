from django import forms

from .models import Lead


class LeadForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = ('email',)

    def save(self, *args, **kwargs):
        super(LeadForm, self).save(*args, **kwargs)

