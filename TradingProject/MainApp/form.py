from django import forms
from MainApp.models import Index 
class UploadFileForm(forms.ModelForm):
    class Meta:
        model=Index
        fields=('timeframe','csvfile') 
             