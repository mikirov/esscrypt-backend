from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    client = models.CharField(max_length=200)
    preview_url = models.URLField(blank=True)  # Optional URL field for project preview
    project_url = models.URLField(blank=True)  # Optional URL field for project link

    def __str__(self):
        return self.name
