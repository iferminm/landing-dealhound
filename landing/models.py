from django.db import models


class Lead(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return self.email

    def __unicode__(self):
        return u'{0}'.format(self.__str__())
