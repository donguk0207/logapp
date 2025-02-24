from django.db import models

# Create your models here.
class PacketLog(models.Model):
    timestamp = models.DateTimeField()
    src_ip = models.GenericIPAddressField()
    dst_ip = models.GenericIPAddressField()
    protocol = models.CharField(max_length=10)
    bytes_in = models.IntegerField()
    bytes_out = models.IntegerField()
    packets_in = models.IntegerField()
    packets_out = models.IntegerField()
    host = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.timestamp} - {self.src_ip} -> {self.dst_ip}"
