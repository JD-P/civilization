from django.core.management.base import BaseCommand, CommandError
from civforum.models import *
from time import time
from datetime import datetime

class Command(BaseCommand):
    help = """Populates initial database with general board, levels of rigor for threads, thread purposes, moods, bantypes, tags."""

    def handle(self, *args, **options):
        now = datetime.utcfromtimestamp(time.time())
        # Create general board
        gboard = Board(title="General",
                       description="A place for threads which don't quite fit under any other board.",
                       creation_date=now,
                       last_activity=now)
        gboard.save()
        pboard = PublicBoard(board=gboard)
        pboard.save()
        # Create levels of rigor
        rigor_levels = (('Polymath',
                         """Academic tone. Half baked ideas are king, quarter baked ideas are emperor."""),
                        ('Casual', 'No requirements beyond engaging text.'),
                        ('Serious', 'Major claims should come with
                        (good) sources.'),
                        ('Citation', 'Most or all claims should come with some source, even if the source is less than ideal.'),
                        ('EffortCitation', 'Most or all claims should come with a good source.'),
                        ('AcademicCitation', 'Most or all claims should come with a good source, participants should explain how they found the source, journal articles heavily preferred over other sources.'))
        for rigor_level in rigor_levels:
            rigor_object  = Rigor(label=rigor_level[0],
                                  description=rigor_level[1])
            rigor_object.save()
        # Create thread purposes
        thread_purposes = (('Shitpost','Garbage humor, trolling, etc.'),
                           ('Collection', 'Collaboration to create a list, album, or other aggregation of items centered around a theme.'),
                           ('Poll', 'A thread to measure the opinion of users on a subject, often accompanied by a survey of some sort.'),
                           ('Proposal', 'An idea of something that forum users should consider implementing or doing.'),
                           ('Conversation', 'A discussion about a topic.'),
                           ('Question', 'A specific query asked to
users with a small number of \'valid\' answers. As distinct from a
collection which has many possible answers and a poll which is less
                           about *the* answer as it is about *other peoples* answers.'),
                           ('Other', 'Something which doesn\'t fall under the predefined thread purposes.'))
        for thread_purpose in thread_purposes:
            thread_purpose_obj = Purpose(name=thread_purpose[0],
                                         description=thread_purpose[1])
            thread_purpose_obj.save()
        # Create post moods
        post_moods = (('Neutral',
                       'No particular emotional inflection.'),
                      ('Angry',
                       'Frustration, rage, flaming, etc.'),
                      ('Sad',
                       'Sorrow, disappointed, dejected, etc.'),
                      ('Joy',
                       'Very happy, excited, cheer, etc.'),
                      ('Confused',
                       'Failed to understand, unsure, questioning, etc.'),
                      ('Fear',
                       'Afraid, shaking, freaking out.'))
        for post_mood in post_moods:
            post_mood_obj = Mood(label=post_mood[0],
                                 description=post_mood[1])
            post_mood_obj.save()

        # Create ban types
        ban_types = (('Permanent',
                      'A long term involuntary ban. (Longer than six months.)'),
                     ('Long',
                      'A medium term involuntary ban. (Longer than three days.)'),
                     ('TimeOut',
                      'A short term involuntary ban. (Three days or less.)'),
                     ('Vacation',
                      'A long term voluntary self ban. (Longer than 1 week.)'),
                     ('Break',
                      'A short term voluntary self ban. (Less than one week.)'))
        for ban_type in ban_types:
            ban_type_obj = BanType(type=ban_type[0],
                                   description=ban_type[1])
            ban_type_obj.save()
