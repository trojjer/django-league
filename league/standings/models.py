from django.db import models


class TeamStanding(models.Model):
    """Represents a team's standing.
    """
    class Meta:
        """
        """
        unique_together = (
            'source_timestamp', 'team_id', 'competition_id', 'season_id',)


    source_timestamp = models.DateTimeField()
    team_id = models.IntegerField()
    competition_id = models.IntegerField()
    season_id = models.IntegerField()
    against = models.IntegerField()
    drawn = models.IntegerField()
    goals_for = models.IntegerField()
    lost = models.IntegerField()
    played = models.IntegerField()
    points = models.IntegerField()
    start_day_position = models.IntegerField()
    won = models.IntegerField()
    away_against = models.IntegerField()
    away_drawn = models.IntegerField()
    away_for = models.IntegerField()
    away_lost = models.IntegerField()
    away_played = models.IntegerField()
    away_points = models.IntegerField()
    away_position = models.IntegerField()
    away_won = models.IntegerField()
    home_against = models.IntegerField()
    home_drawn = models.IntegerField()
    home_for = models.IntegerField()
    home_lost = models.IntegerField()
    home_played = models.IntegerField()
    home_points = models.IntegerField()
    home_position = models.IntegerField()
    home_won = models.IntegerField()
