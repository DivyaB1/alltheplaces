from locations.storefinders.uberall import UberallSpider
from locations.categories import Categories, apply_category


class UnicreditDeSpider(UberallSpider):
    name = "unicredit_de"
    item_attributes = {"brand": "UniCredit", "brand_wikidata": "Q45568"}
    key = "QZ7auxGUWKL0MfAnUOgweafKIwrXPb"

    def parse_item(self, item, location):
        apply_category(Categories.BANK, item)
        yield item
