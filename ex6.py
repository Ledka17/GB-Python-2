import locale

f = open('test_file.txt', 'w', encoding='utf-8')
f.write('сетевое программирование\n')
f.write('сокет\n')
f.write('декоратор\n')
f.close()

with open("test_file.txt") as f:
  def_coding = locale.getpreferredencoding()
  print(def_coding) #US-ASCII

with open("test_file.txt", encoding='utf-8') as f:
  for line in f:
      line = line.rstrip()
      print(line)
#сетевое программирование
#сокет
#декоратор
