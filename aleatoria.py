#!/usr/bin/python3

import webapp
import random

class aleatoria(webapp.webApp):

    def process(self,parsedRequest):
        URL = str(random.randint(0,100000000))
        return ("200 OK", "<html><body><a href= '"+ URL +"'>Dame otra</a></body></html>")
if __name__ == "__main__":
    testWebApp = aleatoria("localhost", 1234)
