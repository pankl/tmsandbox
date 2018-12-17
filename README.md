# tmsandbox
Assignment: Auto test for assurity.

Details:
Using the API given below create an automated test with the listed acceptance criteria:
 
API = https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false
 
Acceptance Criteria:
Name = "Carbon credits"
CanRelist = true
The Promotions element with Name = "Gallery" has a Description that contains the text "2x larger image"
Assuming there's up to one promotion with name "Gallery", if there's more than one the assertion will be made on the first one.


I chose to use python as it's powerful but yet very lightweight and easy to prototype with it.

To run the test from command line from Tests directory: python test_get_by_category_id.py
To change test parameters go to config directory and modify ini file.