from django.db import models
from django.utils.translation import ugettext_lazy as _

from zinnia.models import Entry
import secretballot


class EntryVideo(models.Model):
    """
    Video
    """
    entry = models.ForeignKey(
        Entry,
        related_name='entry_video')
    video = models.CharField(
        _('video'), max_length=500, blank=True,
        help_text=_('HTML code for insertion of video.'))


secretballot.enable_voting_on(Entry)