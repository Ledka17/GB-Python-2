import subprocess as sp

args = ['yandex.ru', 'youtube.com']

s_ping = sp.Popen(args, stdout=sp.PIPE)

for line in s_ping.stdout:
  line = line.decode('cp866').encode('utf-8')
  print(line.decode('utf-8'))
