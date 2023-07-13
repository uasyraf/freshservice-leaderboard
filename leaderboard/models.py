from django.db import models

# Create your models here.
class Agent(models.Model):
    first_name = models.CharField(blank=False)
    last_name = models.CharField(blank=False)
    email = models.CharField(blank=False, unique=True)
    agent_group = models.CharField(blank=False)
    fs_id = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.first_name + self.last_name + '_' + str(self.fs_id)
    
class AverageFirstResponseTime(models.Model):
    average_first_response_time = models.DecimalField(default=0.0)
    ticket_type = models.CharField(choices=['incident', 'inquiry'])
    month = models.DateField(
        blank=False,
        choices=[
            'january',
            'february',
            'march',
            'april',
            'may',
            'june',
            'july',
            'august',
            'september',
            'october',
            'november',
            'december',
        ]
    )
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

class 