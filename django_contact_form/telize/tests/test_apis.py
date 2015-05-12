from mock import patch

from django.test import TestCase

from telize.api.geoip import Geoip


class GeoipTest(TestCase):
    def setUp(self):
        self.geoip = Geoip()

    @patch('telize.api.geoip.requests.get')
    def test_get_geoip_should_return_correct_data(self, mock):
        mock.return_value.json.return_value = {
            u'city': u'Bangkok',
            u'region_code': u'40',
            u'dma_code': u'0',
            u'ip': u'58.137.162.34',
            u'region': u'Krung Thep',
            u'isp': u'CS LOXINFO PUBLIC COMPANY LIMITED',
            u'area_code': u'0',
            u'longitude': 100.5014,
            u'country_code3': u'THA',
            u'continent_code': u'AS',
            u'country_code': u'TH',
            u'offset': u'7',
            u'latitude': 13.754,
            u'timezone': u'Asia/Bangkok',
            u'country': u'Thailand',
            u'asn': u'AS4750'
        }

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
            "timezone": "Asia/Bangkok",
            "region": "Krung Thep",
            "country_code": "TH",
            "isp": "CS LOXINFO PUBLIC COMPANY LIMITED",
            "country": "Thailand",
            "country_code3": "THA",
            "region_code":"40"
        }

        result = self.geoip.get()
        self.assertDictEqual(result, expected)

    @patch('telize.api.geoip.requests.get')
    def test_get_geoip_should_call_telize_api(self, mock):
        self.geoip.get()
        mock.assert_called_once_with('http://www.telize.com/geoip')
