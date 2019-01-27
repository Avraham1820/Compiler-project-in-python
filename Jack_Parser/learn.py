import os
import xml.etree.ElementTree as ET
import lxml
#from lxml import etree

broken_html = "<html><head><title>test<body><h1>page title</h3>"

parser = etree.HTMLParser()

tree   = etree.parse(StringIO(broken_html), parser)

result = etree.tostring(tree.getroot(),pretty_print=True, method="html")



print(result)