# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper

from .models import Ticket, FollowUp, Attachment


class UserSettingsForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False


class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description',
                  'status', 'waiting_for', 'assigned_to')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False


class TicketEditForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'owner', 'description',
                  'status', 'waiting_for', 'assigned_to')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False


class FollowupForm(forms.ModelForm):

    class Meta:
        model = FollowUp
        fields = ('ticket', 'title', 'text', 'user')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False


class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ('file',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False
