from django.forms import ModelForm

from link_shortener.models import Link


class ReceiverLink(ModelForm):
    class Meta:
        model = Link
        fields = ('link',)
