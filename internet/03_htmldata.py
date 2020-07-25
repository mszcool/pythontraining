#
# Example HTML processing
#

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.metacount = 0

    def handle_comment(self, data):
        print("Found comment: ", data)
        pos = self.getpos()
        print("-- location at line %d and position %d " % (pos[0], pos[1]))

    def handle_starttag(self, tag, attrs):
        if tag == 'meta':
            self.metacount += 1
        
        print("Found opening tag: ", tag)
        pos = self.getpos()
        print("-- location at line %d and position %d " % (pos[0], pos[1]))

        if attrs.__len__() > 0:
            print("-- Attributes:")
            for a in attrs:
                print("   - ", a[0], " = ", a[1])
    
    def handle_endtag(self, tag):
        print("Found closing tag: ", tag)
        pos = self.getpos()
        print("-- location at line %d and position %d " % (pos[0], pos[1]))

    def handle_data(self, data):
        if (data.isspace()):
            return
        print("Found data: ", data)
        pos = self.getpos()
        print("-- location at line %d and position %d " % (pos[0], pos[1]))

    def print_and_reset_metacount(self):
        print("Number of metatags: ", self.metacount)
        self.metacount = 0

def main():
    # Create the HTML parser
    parser = MyHTMLParser()
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()
        parser.feed(contents)
        parser.print_and_reset_metacount()

if __name__ == "__main__":
    main()