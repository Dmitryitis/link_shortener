from django.db import models


class Link(models.Model):
    link = models.URLField(verbose_name="Ссылка", max_length=256)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name_plural = 'Ссылки'
        verbose_name = 'Ссылка'
