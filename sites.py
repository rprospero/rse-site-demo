#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import unittest

def page_check(name, version, caller):
    actual = caller()
    if version == actual:
        print(f"{name} ok")
    else:
        print(f"{name} expected {version} but got {actual}")

class SiteChecks(unittest.TestCase):

    def test_dissolve(self):
        version = "1.5.1"

        r = requests.get("https://projectdissolve.com/packages/")
        self.assertEqual(r.status_code, 200)
        soup = BeautifulSoup(r.text, features="html.parser")
        actual = soup.select_one('a[href="#release"]').get_text()
        self.assertEqual(version, actual)

    def test_sasview(self):
        version = "v5.0.6"

        r = requests.get("https://github.com/SasView/sasview/releases")
        self.assertEqual(r.status_code, 200)
        soup = BeautifulSoup(r.text, features="html.parser")
        #Use second entry because current first entry is rc for pre-release
        actual = soup.select('span.ml-1.wb-break-all')[1].get_text().strip()
        self.assertEqual(version, actual)

    def test_mdanse(self):
        import re
        version = "v2.1.1"

        r = requests.get("https://github.com/ISISNeutronMuon/SScanSS-2/releases")
        self.assertEqual(r.status_code, 200)
        soup = BeautifulSoup(r.text, features="html.parser")
        actual = soup.select('span.ml-1.wb-break-all')[0].get_text().strip()
        self.assertEqual(version, actual)

    def test_fitbenchmarking(self):
        import re
        version = "v1.0.0"

        r = requests.get("https://github.com/fitbenchmarking/fitbenchmarking/releases")
        self.assertEqual(r.status_code, 200)
        soup = BeautifulSoup(r.text, features="html.parser")
        actual = soup.select('span.ml-1.wb-break-all')[0].get_text().strip()
        self.assertEqual(version, actual)


if __name__=="__main__":
    unittest.main()
