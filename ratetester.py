import htmllib, formatter
import urllib, htmllib, formatter, re, time, threading, random

class LinksExtractor(htmllib.HTMLParser):
    
    def __init__(self, formatter):
        htmllib.HTMLParser.__init__(self, formatter)
        self.links = []
    
    def start_a(self, attrs):
        if len(attrs) > 0 :
            for attr in attrs :
                if attr[0] == "href":
                    self.links.append(attr[1])
    
    def get_links(self):
        return self.links

excludelist = ["http://buzz.blogger.com/","http://www.blogger.com/go/discuss"]

def piss_off_blogger():
    for x in xrange(99,100000):
        format = formatter.NullFormatter()
        htmlparser = LinksExtractor(format)
        #data = urllib.urlopen("https://www.blogger.com/profile/35217655")
        #data = urllib.urlopen("https://www.blogger.com/profile/5618947")
        data = urllib.urlopen("https://www.blogger.com/profile/"+str(x))
        p = re.compile(r'^https?://.+blog.+\..+')
        htmlparser.feed(data.read())
        htmlparser.close()
        links = htmlparser.get_links()
        print "Loading profile "+str(x)
        if "//support.google.com/websearch/answer/86640" in links:
            print "Hit the rate limiter"
            return

def still_limited():
    format = formatter.NullFormatter()
    htmlparser = LinksExtractor(format)
    #data = urllib.urlopen("https://www.blogger.com/profile/35217655")
    #data = urllib.urlopen("https://www.blogger.com/profile/5618947")
    data = urllib.urlopen("https://www.blogger.com/profile/"+str(x))
    p = re.compile(r'^https?://.+blog.+\..+')
    htmlparser.feed(data.read())
    htmlparser.close()
    links = htmlparser.get_links()
    if "//support.google.com/websearch/answer/86640" in links:
        print "Still behind the rate limiter"
        return True
    return False

delaytimes =[10,15,30,45]

for timetodelay in delaytimes:
    print "Testing delay time of "+str(timetodelay)+" minute(s)"
    piss_off_blogger()
    print "Pissed off Blogger, time to wait"
    time.sleep(timetodelay*60)
    if not still_limited:
        print "No longer limited after "+str(timetodelay)+" minute(s)"
        exit()
    print "Didn't work, we'll try again with a longer delay"
