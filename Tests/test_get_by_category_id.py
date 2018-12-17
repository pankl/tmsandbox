"""Tests for get by category id """
import urllib2
import json
import unittest


class TestByCategoryId(unittest.TestCase):

    def setup(self):
        self.url = "https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false"

    def send_get_request(self,url):
        try:
            self.resp = urllib2.urlopen(url).read()
        except urllib2.HTTPError as err:
            self.fail("There was an error during the request.\nServer returned with error: {0}\n{1}\nFailing the rest of the test.".format(err.code,err.msg))

    def parse_response(self):
        try:
            return json.loads(self.resp)
        except Exception as e:
            self.fail("There was a problem parsing the json response.\n{0}\nFailing the rest of the test.".format(e))

    def test_get_by_category_id(self):
        self.url = "https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false"
        self.send_get_request(self.url)
        parsed_resp = self.parse_response()
        #asserts
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
