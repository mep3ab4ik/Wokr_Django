from django import forms

from chat_app.models import Chat


class ChatMessageForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ['text', 'recipient', 'sender']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2}),
            "sender": forms.HiddenInput(),
            "recipient": forms.HiddenInput(),
        }
