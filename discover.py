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
    if "//support.google.com/websearch/answer/86640" in links:
        print "Hit the rate limiter"
        with open("recordfile.txt","a") as recordfile:
            recordfile.write("Hit rate limiter on "+str(x)+"\n")
        time.sleep(60)
    print links
    for link in links:
        try:
            foundlink = p.search(link).group()
            if not foundlink in excludelist:
                with open("resultsfile.txt","a") as resfile:
                    resfile.write(foundlink+"\n")
                print foundlink
        except:
            pass
    with open("recordfile.txt","a") as recordfile:
        recordfile.write(str(x)+"\n")
    time.sleep(10+random.randrange(0, 10, 2))