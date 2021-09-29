import sys

from geodata.models import RegionModel, DistrictModel, CityModel
from seeds.utils import seed_objects_from_csv


class GeoSeeder:

    def create(self, refresh=False):
        if refresh is True:
            self.truncate_table()

        seed_objects_from_csv('static/seeds/regions.csv', RegionModel)
        seed_objects_from_csv('static/seeds/districts.csv', DistrictModel)
        seed_objects_from_csv('static/seeds/cities.csv', CityModel)

    def truncate_table(self):
        RegionModel.objects.all().delete()
        DistrictModel.objects.all().delete()
        CityModel.objects.all().delete()
        sys.stdout.write("Truncate geo tables ... [OK]\n")
