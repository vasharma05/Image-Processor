from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.userImage)
admin.site.register(models.CentroidImage)
admin.site.register(models.GradientImage)
admin.site.register(models.NegativeImage)
admin.site.register(models.SegmentationImage)
admin.site.register(models.HistogramImage)
admin.site.register(models.GrayscaleImage)
admin.site.register(models.AverageImage)
admin.site.register(models.GaussianImage)
admin.site.register(models.MedianImage)
admin.site.register(models.SobelImage)
