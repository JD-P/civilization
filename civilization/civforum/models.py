from django.db import models

# Create your models here.

class Board(models.Model):
    """Table representing a top level board."""
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField()
    last_activity = models.DateTimeField()
    locked = models.BooleanField(default=False)
    
class ProjectBoard(Board):
    """Unlike a top level board, a project board is a private enclave for a set 
    of members working collaboratively on something. Any member in good standing
    can create a project board. (This feature for example might be restricted from
    new members to prevent its use as an easy denial of service attack.) Because
    it is fundamentally disjoint from the top level board set, it has its own
    separate class which defines the same data for the project boards."""
    author = models.ForeignKey('User')
    description = models.CharField(max_length=1024) # Prevent UI screw

class PBMembers(models.Model):
    """Table specifying who is and is not part of a project board. Project
    boards have a specific set of users and are not generally visible to those 
    who are not invited."""
    member = models.ForeignKey('User')
    role = models.CharField(max_length=50, null=True)
    join_date = models.DateTimeField()
    
class Thread(models.Model):
    """Table representing a forum thread."""
    board = models.ForeignKey('Board')
    title = models.CharField(max_length=125)
    author = models.ForeignKey('User')
    rigor = models.ForeignKey('Rigor')
    posts = models.IntegerField()
    creation_date = models.DateTimeField()
    last_activity = models.DateTimeField()
    locked = models.BooleanField(default=False)
    
class TBody(models.Model):
    """A table of thread bodies. One thread can have multiple revisions of 
    the same textual body. This is all the version control I'll be implementing
    for the prototype."""
    thread = models.ForeignKey('Thread')
    version = models.DateTimeField()
    body = models.TextField()
    
class Purpose(models.Model):
    """Table to store the different options to put in under the purpose field for
    a thread."""
    name = models.CharField(max_length=50)
    description = models.TextField()

class Prediction(models.Model):
    """A prediction. One that might be made as part of a forum post or on its own."""
    text = models.CharField(max_length=2048)
    judge = models.ForeignKey('User')
    creation_date = models.DateTimeField()
    judge_date = models.DateTimeField(null=True)
    probability = models.DecimalField()
    outcome = models.BooleanField(null=True, default=None)
    
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

class TPost(models.Model):
    """A forum thread post. May have predictions and up to three 100kb attachments."""
    author = models.ForeignKey('User')
    creation_date = models.DateTimeField()
    body = models.CharField(max_length=57344)
    mood = models.ForeignKey('Mood')

class TPostPrediction(models.Model):
    """A prediction associated with a post. This goes into the general table of
    predictions so this table is just a link to extant predictions in that one."""
    post = models.ForeignKey('TPost')
    prediction = models.ForeignKey('Prediction')

class TPostAttachment(models.Model):
    """A file attachment associated with a post. A post can only have three of these,
    and no more than 100kb file size per attachment. This has more to do with the sparse
    space I have on my servers than any particular animus against big files."""
    post = models.ForeignKey('TPost')
    file = models.FileField(upload_to='/attachments', max_length=102400)
    
class Ban(models.Model):
    """A ban table that is checked at login time to see if a user is still allowed
    to access the system. Note that not all things in the ban table are *bans* per se.
    For example a user might request to have themselves disallowed from using the site
    for a few hours so they can get things done. Or even an entire week."""
    user = models.ForeignKey('User')
    ban_type = models.ForeignKey('BanType')
    ban_reason = models.TextField()
    ban_date = models.DateTimeField()
    ban_lifted = models.DateTimeField()
    
class BanType(models.Model):
    """A table of types of bans. These are used not just to categorize the kind of
    bans which are handed out by moderators but to change the template which is 
    shown to users when they excuse themselves from the forum for however long. 
    This includes the login fail messages shown to a 'banned' user, and the message
    which is given to the community about their absence. For example a user on a two
    week vacation would not want the "user was banned" message shown to explain to
    other users where they are when they look at their profile."""
    type = models.CharField(max_length=50)
