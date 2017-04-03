from django.db import models

# Create your models here.

class Board(models.Model):
    """Table representing a top level board."""
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_activity = models.DateField()

class Thread(models.Model):
    """Table representing a forum thread."""
    title = models.CharField(max_length=125)
    author = models.ForeignKey('User')
    rigor = models.ForeignKey('Rigor')
    posts = models.IntegerField()
    last_activity = models.DateField()

class Purpose(models.Model):
    """Table to store the different options to put in under the purpose field for
    a thread."""
    name = models.CharField(max_length=50)
    description = models.TextField()

class Tag(models.Model):
    """Table to store all the tags which are in use on any thread."""
    string = models.CharField(max_length=50)
    
class RTag(models.Model):
    """Table to store the different restricted tags which are mandatory to use
    when creating a thread."""
    tag = models.ForeignKey('Tag')
    
class TPurpose(models.Model):
    """A thread purpose. A thread can have more than one purpose associated with it,
    so they go in a separate table."""
    thread = models.ForeignKey('Thread',on_delete=models.CASCADE)
    purpose = models.ForeignKey('Purpose')
    
class TRTag(models.Model):
    """A restricted/mandatory thread tag. A thread can have more than one rtag 
    associated with it, so they go in a separate table."""
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)
    rtag = models.ForeignKey('RTag')


