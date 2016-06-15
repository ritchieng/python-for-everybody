# Naming code
import xml.etree.ElementTree as ET

# ''' represents whole string
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

# Parse string: de-serialization
tree = ET.fromstring(data)

# Find tag 'name' --> text
print 'Name:',tree.find('name').text

# Find tag 'email' --> get 'hide' attribute
print 'Attr:',tree.find('email').get('hide')

print 'Phone:', tree.find('phone').text
print 'Phone type:', tree.find('phone').get('type')