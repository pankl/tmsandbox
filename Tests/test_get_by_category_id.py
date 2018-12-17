"""Tests for get by category id """
import urllib2
import json
import unittest
import ConfigParser


class TestByCategoryId(unittest.TestCase):

    def setUp(self):
        """This is the initializer of the test, all the hardcoded test values going into here"""
        configParser = ConfigParser.ConfigParser()
        try:
            configParser.read('../Config/TestByCategoryId.ini')
        except Exception as e:
            self.fail("Failed reading test configuration file.\n{0}".format(e))
        self.url = configParser.get('6327', 'Url')
        self.nameToAssert = configParser.get('6327', 'Name')
        self.canRelist = configParser.get('6327', 'CanRelist')
        self.promotionName = configParser.get('6327', 'PromotionName')
        self.promotionDescription = configParser.get('6327', 'PromotionDescription')

    def send_get_request(self,url):
        try:
            self.resp = urllib2.urlopen(url).read()
        except urllib2.HTTPError as err:
            self.fail("There was an error during the request.\nServer returned with error: {0}\n{1}\nFailing the rest of the test."
                      .format(err.code,err.msg))

    def parse_response(self):
        try:
            return json.loads(self.resp)
        except Exception as e:
            self.fail("There was a problem parsing the json response.\n{0}\nFailing the rest of the test.".format(e))

    def assert_based_on_specific_criteria(self, response, nameToAssert, canRelist, promotionName, promotionDescription):

        self.assertEqual(nameToAssert,response['Name'],"Expected Carbon credits got {0}".format(response['Name']))
        self.assertTrue(response['CanRelist'], "Expected 'Can Relist' attribute to be True, got False") if canRelist \
            else self.assertFalse(response['CanRelist'], "Expected 'Can Relist' attribute to be False, got True")

        for item in response['Promotions']:
            promotion = None
            if item['Name'] == promotionName:
                promotion = item
                break

        self.fail("Couldn't find promotion with name '{0}'".format(promotionName)) if promotion is None \
            else self.assertIn(promotionDescription,promotion['Description'],
                               "Couldn't find {0} in the promotion description, got {1}".format(promotionDescription,promotion['Description']))

    def test_get_by_category_id(self):

        """The actual test steps divided logicaly into three groups, make the call, parse response do asserts. Resembles to BDD format"""
        print "Making the call to {0}".format(self.url)
        self.send_get_request(self.url)
        print "Parsing response"
        parsed_resp = self.parse_response()
        print "Doing asserts"
        self.assert_based_on_specific_criteria(parsed_resp, self.nameToAssert, self.canRelist, self.promotionName, self.promotionDescription)




if __name__ == '__main__':
    unittest.main()
