import urllib
import sys
from HTMLParser import HTMLParser

def open_page(contestID, problemID):
    print "Trying to connect to the server..."
    pageURL = "http://www.codeforces.com/contest/" + contestID + "/problem/" + problemID
    print pageURL
    page = urllib.urlopen(pageURL)
    print "Connected to the server."
    print "Fetching Problem page..."
    source = page.read()

    return source

class problemPageParser(HTMLParser):

    inside_sample_tests = 0
    branches = 0
    test_cases_list = []

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[1] == 'sample-tests':
                self.inside_sample_tests = 1
                return
        if self.inside_sample_tests == 1:
            self.branches = self.branches + 1
    def handle_endtag(self, tag):
        if(self.inside_sample_tests == 1):
            self.branches = self.branches - 1
        if self.branches == -1:
            self.inside_sample_tests = 0

    def handle_data(self, data):
        if(self.inside_sample_tests == 1):
            self.test_cases_list.append(data)

    def return_data(self):
        return self.test_cases_list[1:]