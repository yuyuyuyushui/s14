import xml.etree.ElementTree as ET

root = ET.parse('xml_test.xml').getroot()
print(root.tag)

# for child in root:
#     #print(child.tag, child.attrib)
#     for i in child:
#         if i.tag == 'year':
#             print(i.tag, i.text, i.attrib)
for node in root.iter('year'):#只遍历‘year’节点
    print(node.tag, node.text)

