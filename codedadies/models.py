from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length = 500)             #creating of data in models
    created = models.DateTimeField(auto_now = True)

    def __str__(self):                                #show database form models as a name not "search object (id=nr)"
        return (self.search)

    class Meta:
        verbose_name_plural = 'Searches'      # add "s" in the end of name class "Search" in admin API("searches")

