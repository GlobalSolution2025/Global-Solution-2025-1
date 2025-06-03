from django.db import models

class SensorData(models.Model):
    temperatura = models.FloatField()
    umidade = models.FloatField()
    mq2 = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.temperatura}°C, {self.umidade}%, MQ2: {self.mq2}"

