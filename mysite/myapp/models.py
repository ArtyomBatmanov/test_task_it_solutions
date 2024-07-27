from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    views_count = models.PositiveIntegerField(default=0)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position"]
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title
