from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    preview_image_url = models.URLField(max_length=255)
    content_image_urls = models.JSONField(default=list)  # Store content image URLs as a list
    github_url = models.URLField(max_length=255)
    deployed_project_url = models.URLField(max_length=255)

    def __str__(self):
        return self.name
