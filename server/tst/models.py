from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Team(models.Model):
    date = models.DateField()
    players = models.ManyToManyField(Player, related_name="teams")

class Match(models.Model):
    date = models.DateField()
    team_a = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_a")
    team_b = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_b")
    score_a = models.IntegerField()
    score_b = models.IntegerField()

