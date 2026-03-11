from django.forms import ModelForm

from elements.models import Element


class ElementForm(ModelForm):
    class Meta:
        model = Element
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })
