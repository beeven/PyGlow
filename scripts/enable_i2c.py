#!/usr/bin/env python

modules_file = open('/etc/modules','r+')
mf_lines = modules_file.read().split('\n')
mf_lines = list(filter(lambda l:l.find('i2c-dev') == -1 and l.find('i2c-bcm2708')==-1,mf_lines))

mf_lines.append('i2c-dev')
mf_lines.append('i2c-bcm2708')
data = '\n'.join(mf_lines)

modules_file.seek(0)
modules_file.writelines(data)
modules_file.truncate()
modules_file.close()


blacklist_file = open('/etc/modprobe.d/raspi-blacklist.conf','r+')
bf_lines = blacklist_file.read().split('\n')
for line in bf_lines:
    if line.startswith('blacklist') and (line.find('spi-bcm2708') != -1 or line.find('i2c-bcm2708') != -1):
        bf_lines[bf_lines.index(line)] = '# ' + line
data = '\n'.join(bf_lines)
blacklist_file.seek(0)
blacklist_file.write(data)
blacklist_file.truncate()
blacklist_file.close()
