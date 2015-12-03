from django.views.generic.list import ListView

from .models import TeamStanding


class StandingsListView(ListView):
    """List the teams and their standings.
    """
    model = TeamStanding
