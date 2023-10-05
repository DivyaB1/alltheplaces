import scrapy

from locations.items import Feature
from locations.categories import Categories, apply_category


class QStartSESpider(scrapy.Spider):
    name = "qstar_se"
    start_urls = ["https://qstar-backend-prod.herokuapp.com/api/v2/stations/qstar"]

    brand_mapping = {
        "Qstar": {"brand": "Qstar", "brand_wikidata": "Q10647961"},
        "Pump": {"brand": "Pump"},
        "Bilisten": {"brand": "Bilisten"},
    }

    def parse(self, response, **kwargs):
        for store in response.json():

            item =  Feature(
                {
                    "ref": store.get("id"),
                    "name": store.get("name"),
                    "street_address": store.get("address"),
                    "brand": self.brand_mapping.get(store.get("brand")).get("brand"),
                    "brand_wikidata": self.brand_mapping.get(store.get("brand")).get("brand_wikidata"),
                    "postcode": store.get("postcode"),
                    "city": store.get("city"),
                    "phone": store.get("phone"),
                    "lat": float(store.get("latitude")),
                    "lon": float(store.get("longitude")),
                }
            
            )

            apply_category(Categories.FUEL_STATION, item)
            yield item


            
