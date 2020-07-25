#
# Working with XML Data
#

import xml.dom.minidom

def main():
    print("Welcome to XML")

    # Parsing the XML data
    doc = xml.dom.minidom.parse("samplexml.xml")

    # Print out the document node and the name of the first child tag
    print(doc.nodeName)
    print(doc._get_firstChild().tagName)    # weird, that works and
    print(doc.firstChild.tagName)           # that works as well, but didn't have IntelliSense

    # Get a list of XML tags from the document and print each one
    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))

    # Create a new XML Tag and add it to the document
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "jQuery")
    doc.firstChild.appendChild(newSkill)
    
    f = open("samlexml2.xml", "w+")
    if f.mode == "w+":
        doc.writexml(f)
        f.close()
    else:
        print("Failed opening file...")

if __name__ == "__main__":
    main()