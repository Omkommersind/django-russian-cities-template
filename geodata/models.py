from django.db import models

from backend.db.models import BaseModel


class RegionModel(BaseModel):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название региона/области')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_geodata_regions'
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class DistrictModel(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Название района')
    region = models.ForeignKey(RegionModel, on_delete=models.PROTECT, verbose_name='Регион/Область',
                               related_name='districts')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = [['title', 'region']]
        db_table = 'app_geodata_districts'
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class CityModel(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Название города')
    region = models.ForeignKey(RegionModel, on_delete=models.PROTECT, verbose_name='Регион/Область',
                               related_name='cities', null=True, blank=True)
    district = models.ForeignKey(DistrictModel, on_delete=models.PROTECT, verbose_name='Район', null=True, blank=True,
                                 related_name='cities')

    def __str__(self):
        return f'{self.region.title}, {self.title}'

    class Meta:
        unique_together = [['title', 'region', 'district']]
        db_table = 'app_geodata_cities'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['region__title']

