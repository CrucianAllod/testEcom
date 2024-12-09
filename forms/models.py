from djongo import models

class FormsTemplate(models.Model):
    name = models.CharField(max_length=255)
    fields = models.JSONField()

    class Meta:
        db_table = 'form_templates'