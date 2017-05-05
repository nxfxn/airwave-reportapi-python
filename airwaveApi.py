import requests, csv
import xml.etree.ElementTree as ET

with open('report.csv', 'wb') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["AP ID","IP", "MAC", "Model", "Name", "Controller ID", "Mode", "Firmware"])

data = 'credential_0=xxxxxx&credential_1=xxxxxxxxx&destination=/&login=Log In'
headers={'Content-Type': 'application/x-www-form-urlencoded','Cache-Control':'no-cache'}

ampsession = requests.Session()
loginamp = ampsession.post('https://xxx.xxx.xxx.xxx/LOGIN',headers=headers, data=data, verify=False)

result=ampsession.get('https://xxx.xxx.xxx.xxx/ap_list.xml',headers=headers, verify=False)

aplist = result.content

tree=ET.fromstring(aplist)

for i in tree.iter('ap'):
    id=i.attrib.values()[0]
    ml=[]
    
    ml.append(id)
    
    if i.find('name')!=None:
        name=i.find('name').text
        ml.append(name)
    else: 
        name=" "
        ml.append(name)
    
    if i.find('lan_ip')!=None:
        ip=i.find('lan_ip').text
        ml.append(ip)
    else: 
        ip=" "    
        ml.append(ip)
    
    if i.find('lan_mac')!=None:
        mac=i.find('lan_mac').text
        ml.append(mac)
    else: 
        mac=" "
        ml.append(mac)
    
    if i.find('model')!=None:
        model=i.find('model').text
        ml.append(model)
    else: 
        model=" "
        ml.append(model)    
    
    if i.find('controller_id')!=None:
        controller_id=i.find('controller_id').text
        ml.append(controller_id)
    else: 
        controller_id=" "
        ml.append(controller_id)
    
    if i.find('operating_mode')!=None:
        op_mode=i.find('operating_mode').text
        ml.append(op_mode)
    else: 
        op_mode=" "
        ml.append(op_mode)    
    
    if i.find('firmware')!=None:
        firmware=i.find('firmware').text
        ml.append(firmware)
    else: 
        firmware=" "
        ml.append(firmware)
        
    with open('report.csv', 'a') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(ml)


    
