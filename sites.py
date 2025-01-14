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

    def test_mdanse(self):
        import re
        version = "1.5.2"

        r = requests.get("https://www.isis.stfc.ac.uk/Pages/MDANSEproject.aspx")
        self.assertEqual(r.status_code, 200)
        soup = BeautifulSoup(r.text, features="html.parser")
        result = [re.search("version (.....)", line.get_text().strip()).group(1)
                  for line in soup.select('p')
                  if "Download latest" in line.get_text().strip()][0]
        self.assertEqual(version, result)

    def test_sasview(self):
        version = "v5.0.6"

        r = requests.get("https://github.com/SasView/sasview/releases")
        self.assertEqual(r.status_code, 200)
        soup = BeautifulSoup(r.text, features="html.parser")
        #Use second entry because current first entry is rc for pre-release
        actual = soup.select('span.ml-1.wb-break-all')[1].get_text().strip()
        self.assertEqual(version, actual)

    def test_sscanss(self):
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

    def test_mantid(self):
        import re
        version = "v6.9.1"

        r = requests.get("https://www.mantidproject.org/installation/index")
        self.assertEqual(r.status_code, 200)
        soup = BeautifulSoup(r.text, features="html.parser")
        actual = soup.select('#latest-release p strong')[0].get_text().strip()
        self.assertEqual(version, actual)


if __name__=="__main__":
    unittest.main()
