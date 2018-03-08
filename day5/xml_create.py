import xml.etree.ElementTree as ET#创建XML文件

new_xml = ET.Element('namelist')
name = ET.SubElement(new_xml,'name',attrib={'enrolled':'yes'})
age = ET.SubElement(name, 'age', attrib={'checkd':'no'})
sex = ET.SubElement(name,'sex',attrib={'luo':'liu'})
sex.text = 'man'
age.text = '66'
et = ET.ElementTree(new_xml)
et.write('test.xml',encoding='utf-8',xml_declaration=True)