from django.forms import ModelForm

from .models import Mission


class MissionForm(ModelForm):
    class Meta:
        model = Mission
        fields = '__all__'
        help_texts = {
            'mission_date': '格式示例：2019-12-22 13:30',
        }