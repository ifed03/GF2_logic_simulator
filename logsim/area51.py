device_property = ('0201110')
print ([i for i in str(device_property) if i not in ['0', '1']])

'''
if str(device_property) >= '1'*len(str(device_property)):
    print ('This is not a valid binary waveform')
else: 
    print ('11111111'<='1'*len(str(device_property)))

print (str(device_property)[0].isdigit())'''
