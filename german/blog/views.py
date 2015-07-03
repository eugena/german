from secretballot.views import vote as vote_view
from zinnia.models import Entry


def like(request, entry_id, vote):
    """
    Likes
    """
    try:
        vote = int(vote)
    except ValueError:
        vote = None
    return vote_view(request, Entry, entry_id, vote,  mimetype='application/json')

