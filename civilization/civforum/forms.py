from django import forms
from django.urls import reverse_lazy
from civforum.models import *

from django.db.utils import OperationalError
#TODO:Fix this dirty dirty hack
try:
    boards = [(board.board.id, board.board.title) for board in
              PublicBoard.objects.all()]
    
    rigors = [(rigor.id, rigor.label) for rigor in Rigor.objects.all()]

    purposes = [(purpose.id, purpose.name)
                for purpose in Purpose.objects.all()]
    moods = [(mood.id, mood.label) for mood in Mood.objects.all()]
except OperationalError:
    print("Models have not been migrated yet, please migrate them before use.")
    (boards, rigors, purposes, moods) = ([],[],[],[])
    

class NewThreadRedirectForm(forms.Form):
    purpose = forms.ChoiceField(label="Purpose",
                                choices=purposes)
    
class NewThreadForm(forms.Form):
    board_id = forms.ChoiceField(label="Board",
                                 choices=boards)
    title = forms.CharField(label="Title",
                            max_length=125)
    rigor_id = forms.ChoiceField(label="Rigor Level",
                                 choices=rigors)
    tbody = forms.CharField(label="Body",
                            max_length=57344,
                            widget=forms.Textarea)
    tags = forms.CharField(label="Tags",
                           max_length=2048)
    
class NewPostForm(forms.Form):
    mood = forms.ChoiceField(label="Mood",
                             choices=moods)
    body = forms.CharField(label="Body")
    
class SimpleSearchForm(forms.Form):
    """Form for the basic search as might be added to a board listing."""
    searchbar = forms.CharField(label="Search")

class ExportForm(forms.Form):
    """Form to set options for exporting a users data."""
    output_format = forms.ChoiceField(label="Output Format",
                                      choices=[("xml","XML"), ("json","JSON")])
