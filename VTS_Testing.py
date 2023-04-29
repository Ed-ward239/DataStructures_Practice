#  *(c) Copyright 2018 - 2020 Visa. All Rights Reserved.**
#
#  *NOTICE: The software and accompanying information and documentation (together, the “Software”) remain the property of and are proprietary to Visa and its suppliers and affiliates. The Software remains protected by intellectual property rights and may be covered by U.S. and foreign patents or patent applications. The Software is licensed and not sold.*
#
#  * By accessing the Software you are agreeing to Visa's terms of use (developer.visa.com/terms) and privacy policy (developer.visa.com/privacy).In addition, all permissible uses of the Software must be in support of Visa products, programs and services provided through the Visa Developer Program (VDP) platform only (developer.visa.com). **THE SOFTWARE AND ANY ASSOCIATED INFORMATION OR DOCUMENTATION IS PROVIDED ON AN “AS IS,” “AS AVAILABLE,” “WITH ALL FAULTS” BASIS WITHOUT WARRANTY OR  CONDITION OF ANY KIND. YOUR USE IS AT YOUR OWN RISK.** All brand names are the property of their respective owners, used for identification purposes only, and do not imply product endorsement or affiliation with Visa. Any links to third party sites are for your information only and equally  do not constitute a Visa endorsement. Visa has no insight into and control over third party content and code and disclaims all liability for any such components, including continued availability and functionality. Benefits depend on implementation details and business factors and coding steps shown are exemplary only and do not reflect all necessary elements for the described capabilities. Capabilities and features are subject to Visa’s terms and conditions and may require development,implementation and resources by you based on your business and operational details. Please refer to the specific API documentation for details on the requirements, eligibility and geographic availability.*
#
#  *This Software includes programs, concepts and details under continuing development by Visa. Any Visa features,functionality, implementation, branding, and schedules may be amended, updated or canceled at Visa’s discretion.The timing of widespread availability of programs and functionality is also subject to a number of factors outside Visa’s control,including but not limited to deployment of necessary infrastructure by issuers, acquirers, merchants and mobile device manufacturers.*
#

import datetime
import json
import logging
import requests
import sys
import os

# DEBUG = False
DEBUG = True

# helloworld
# Sample Code for Two-Way (Mutual) SSL

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPSConnection.debuglevel = 0


logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

print("START Sample Code for Two-Way (Mutual) SSL")

print(datetime.datetime.now())
date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

url = 'https://sandbox.api.visa.com/vdp/helloworld'
headers = {'API Test'}
body = {}

payload = json.loads('''{}
''')

# User ID & Password can be found in API dashboard

user_id = 'XL93JY4UD5EYPG2ANN8921cjXJ5E88l_k4fMIWJH7PRNkW7OM'
password = 'jTdpxH55P8eWG8dx5U0A21dnnFQ1eh6fV20'

# key.pem file must download right after API registration (Ex: key_83d11ea6-a22d-4e52-b310-e0558816727d.pem)
# cert.pem file can be downloaded in API credentials (Ex: cert.pem)

cert = sys.path.append(os.path.abspath("C:\Users\24hou\Downloads\cert.pem"))
key = sys.path.append(os.path.abspath("C:\Users\24hou\Downloads\key_ea4f6084-af38-4d09-a2a2-cdfb653e16f6.pem"))

timeout = 10

try:
    response = requests.get(url,
                            # verify = ('put the CA certificate pem file path here'),
                            cert=(cert, key),
                            headers = headers,
                            auth=(user_id, password),
                            data = body,
                            json = payload,
                            timeout = timeout,
                            #if DEBUG: print (response.text)
                            )
except Exception as e:
    print(e)

if DEBUG: print(response.headers)
if DEBUG: print(response.content)

var1 = str(response.status_code)
var2 = '200'
msg = " Two-Way (Mutual) SSL test failed"
assert var1 == var2, msg
print("END Sample Code for Two-Way (Mutual) SSL\n\n")
