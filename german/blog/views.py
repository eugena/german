from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.template import loader
from secretballot.views import vote
from secretballot.models import Vote
from zinnia.models import Entry


def like(request, id, update):
    """
    Like
    """
    mimetype = 'application/json'
    if update:
         return vote(request, Entry, id, 1, can_vote_test=None,
         redirect_url=None, template_name=None, template_loader=loader,
         extra_context=None, context_processors=None, mimetype=mimetype)
    else:
        try:
            votes = Vote.objects.filter(
                content_type=ContentType.objects.get_for_model(Entry), object_id=id).count()
            body = '{"num_votes": %d}' % votes
        except:
            body = '{"num_votes": ""}'
        return HttpResponse(body, content_type=mimetype)
