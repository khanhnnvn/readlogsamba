#!/usr/bin/env python
 
with open('x.log') as f:
    data = f.readlines()
    for item in data:
        item = item.replace('\n', '')
        if len(item) != 0:
            a = item.split()
            b = a[5].split("|")
            try:
                print '---------------------------------'
                print 'Ngay ket noi:', a[2], a[1], a[0]
                print 'Ten may tinh: ', b[1]
                print 'Dia chi IP: ', b[2]
                print 'Action: ', b[4]
                print 'File: ', b[7]
		print '---------------------------------'
            except IndexError:
                print 'None'
    f.close()

