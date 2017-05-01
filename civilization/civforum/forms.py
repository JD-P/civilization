from django import forms
from civforum.models import *


boards = [(board.board.id, board.board.title) for board in
          PublicBoard.objects.all()]

rigors = [(rigor.id, rigor.label) for rigor in Rigor.objects.all()]

purposes = [(purpose.id, purpose.name) for purpose in Purpose.objects.all()]

class NewThreadForm(forms.Form):
    board_id = forms.ChoiceField(label="Board",
                                 choices=boards)
    title = forms.CharField(label="Title",
                            max_length=125)
    purpose_id = forms.ChoiceField(label="Purpose",
                                   choices=purposes)
    rigor_id = forms.ChoiceField(label="Rigor Level",
                                 choices=rigors)
    tbody = forms.CharField(label="Body",
                            max_length=57344,
                            widget=forms.Textarea)
    tags = forms.CharField(label="Tags",
                           max_length=2048)
