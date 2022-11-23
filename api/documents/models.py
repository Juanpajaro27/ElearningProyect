from django.db import models


# Create your models here.
class Users(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, null=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "%s %s %s" % (self.first_name, self.last_name, self.email)


class Repositories(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        Users, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "%s %s" % (self.name, self.created_at)


class Documents(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, null=False)
    name = models.CharField(max_length=100)
    rep_id = models.ForeignKey(Repositories, on_delete=models.CASCADE)
    file = models.FileField(null=False, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "%s %s" % (self.name, self.added_at)
