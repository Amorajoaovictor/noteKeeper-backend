from django.db import models
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class TipoDeNota(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=20000)
    pub_date = models.DateTimeField("date published")
    type = models.ForeignKey(TipoDeNota, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
