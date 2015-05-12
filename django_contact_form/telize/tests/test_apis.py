from django.test import TestCase

from telize.api.geoip import Geoip


class GeoipTest(TestCase):
    def test_get_geoip_should_return_correct_data(self):
        expected = {
            "longitude": 100.5014,
            "latitude": 13.754,
            "asn": "AS4750",
            "offset": "7",
            "ip": "58.137.162.34",
            "area_code": "0",
            "continent_code": "AS",
            "dma_code": "0",
            "city": "Bangkok",
            "timezone": "Asia\/Bangkok",
            "region": "Krung Thep",
            "country_code": "TH",
            "isp": "CS LOXINFO PUBLIC COMPANY LIMITED",
            "country": "Thailand",
            "country_code3": "THA",
            "region_code":"40"
        }

        geoip = Geoip()
        result = geoip.get()
        self.assertDictEqual(result, expected)
