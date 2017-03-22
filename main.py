#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
    fortune_list = ["The wise man doesn't listen to cookies",
    "A Tiger with a fully belly is a friend",
    "My boss is a jerk",
    "Something fortuitous will befall you soonish",
    "Look behind you"
    ]
    index = random.randint(0,4)
    return fortune_list[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>"+getRandomFortune()+"</strong>"
        fortune_sen ="Your fortune: "+fortune
        fortune_p = "<p>"+fortune_sen+"</p>"

        lucky_number = "<strong>"+str(random.randint(1,100))+"</strong>"
        lucky = 'Your Lucky Number is '+ lucky_number
        lucky_p = "<p>"+lucky+"</p>"

        another_cookie = "<button><a href='.'><strong><em>One more couldn't hurt...</strong></em></a></button>"

        content = header + fortune_p + lucky_p + another_cookie
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
