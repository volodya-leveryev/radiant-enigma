from django.db import models


class EducationPlan(models.Model):
    name = models.CharField('название', max_length=64)
    file = models.FileField('файл', upload_to='edu_plan/')

    class Meta:
        verbose_name = 'учебный план'
        verbose_name_plural = 'учебные планы'

    def __str__(self):
        return self.name
