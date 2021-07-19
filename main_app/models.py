from django.db import models

COMMUNITIES = (
  ('None', 'Community Affiliation'),
  ('L', 'Lesbian'),
  ('G', 'Gay'),
  ('B', 'Bisexual'),
  ('T','Transgender'),
  ('Q', 'Queer')
)

class Community(models.Model):
  community = models.CharField(
    choices=COMMUNITIES,
    default=COMMUNITIES[0][0],
    max_length=20
  )

  def __str__(self):
    return f"{self.community}"


class Queero(models.Model):
  name = models.CharField(max_length=100)
  occupation = models.TextField(max_length=2000)
  biography = models.TextField(max_length=2000)
  legacy = models.TextField(max_length=2000)
  communities = models.ManyToManyField(Community)

  def __str__(self):
    return f"{self.name}"


class Quotes(models.Model):
  quote = models.TextField(max_length=2000)  
  queero = models.ForeignKey(Queero, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.quote}"







