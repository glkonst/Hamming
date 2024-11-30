f = open('input2.txt', 'r').readline().strip(' ')
x_list = [int(i) for i in f]  #Преобразуем строку в список чисел

#Добавляем контрольные биты, т.е. дописываем нули
for i in range(0, 20 + 1):
  if (2**i <= len(x_list)):
    x_list.insert(2**i - 1, 0)
  else:
    break

#Заполняем контрольные биты, ставим 1 или 0
for cycle in range(1, i + 1):
  sum_list = []
  for a in range(0, len(x_list), (2**cycle)):
    for bit_num in range(a, a + 2**(cycle - 1)):
      try:
        sum_list.append(x_list[bit_num + (2**(cycle - 1) - 1)])
      except:
        ...
  if sum(sum_list) % 2 == 1:
    x_list[2**(cycle - 1) - 1] = 1
  else:
    x_list[2**(cycle - 1) - 1] = 0

#Преобразуем список в строку и печатаем это
x = [str(l) for l in x_list]
x = ''.join(x)
print(' x=', x)

#Записываем результат в файл output.txt
file = open('output.txt', 'w')
file.writelines('Сообщение, преобразованное по алгоритму Хэмминга (т.е. с дполнительным кодом): ' + '\n' +x)
file.close()

#=========================================================================================

#Получаем сообщение с контрольными битами в файле received.txt (В нём может быть искажение бита)
#Открываем файл received.txt и записываем его в список чисел
r = open('recieved.txt', 'r').readline().strip(' ')
r_list = [int(i) for i in r]

#Заменяем контрольные биты на нули
for ir in range(0, 20 + 1):
  if (2**ir <= len(r_list)):
    r_list[2**ir - 1] = 0
  else:
    break

#Заполняем контрольные биты полученного сообщения аналогично, ставим 1 или 0
for cycle in range(1, ir + 1):
  sum_list = []
  for a in range(0, len(r_list), (2**cycle)):
    for bit_num in range(a, a + 2**(cycle - 1)):
      try:
        sum_list.append(r_list[bit_num + (2**(cycle - 1) - 1)])
      except:
        ...
  if sum(sum_list) % 2 == 1:
    r_list[2**(cycle - 1) - 1] = 1
  else:
    r_list[2**(cycle - 1) - 1] = 0

error = []  #Список индексов ошибочных контрольных бит

#Сравниваем отправленные контрольные биты из output.txt и полученные из received.txt

#Это вариант если в файле received.txt ошибок нет
if all(r_list[2**degree - 1] == x_list[2**degree - 1] for degree in range(0, ir)):
  print('\n', 'ОШИБОК в полученном коде НЕТ')

  #Убираем контрольные биты из исправленного сообщения
  for ir in range(0, 20 + 1):
    if (2**ir <= len(r_list)):
      r_list[2**ir - 1] = 'x'
    else:
      break

  rr = [str(l) for l in r_list]
  re_hamm = ''.join(rr)
  re_hamm = re_hamm.replace('x', '')
  print('\n', 'Сообщение без дополнительного кода:', '\n',re_hamm)

  #file = open('received.txt', 'w')
  #file.write(r + '\n' + '\n' + 'ОШИБОК в полученном коде НЕТ' +'\n' + '\n'+ 'Сообщение без дополнительного кода:' + '\n'+ re_hamm)
  #file.close()

#Это вариант если в файле received.txt ошибка есть
else:
  for degree in range(0, ir):
    if r_list[2**degree - 1] == x_list[2**degree - 1]:
      ...
    else:
      error.append(2**degree)  #Добавляем в список error индексы ошибочных контрольных бит

  s_err = sum(error)  #s_err - это номер ошибочного бита
  print('\n', 'В полученном коде ЕСТЬ ОШИБКА на позиции:', '\n', str(s_err))

  #Исправляем искажённый бит
  if r_list[s_err - 1] == 0:
    r_list[s_err - 1] = 1
  else:
    r_list[s_err - 1] = 0

  #Записываем исправленное сообщение, но ещё с контрольными битами
  rec = [str(l) for l in r_list]
  rec = ''.join(rec)
  print('\n', 'Сообщение с дополнительным кодом с исправленной ошибкой:', '\n',rec)

  #Убираем контрольные биты из исправленного сообщения
  for ir in range(0, 20 + 1):
    if (2**ir <= len(r_list)):
      r_list[2**ir - 1] = 'x'
    else:
      break

  rr = [str(l) for l in r_list]
  re_hamm = ''.join(rr)
  re_hamm = re_hamm.replace('x', '')
  print('\n', 'Сообщение с исправленной ошибкой без дополнительного кода:', '\n',re_hamm)

  #Записываем это всё в файл received.txt
  #file = open('received.txt', 'w')
  #file.write(str(r) + '\n' + '\n' + 'В полученном коде ЕСТЬ ОШИБКА на позиции: ' +'\n' + str(s_err) + '\n' + '\n' +'Сообщение с дополнительным кодом с исправленной ошибкой:' + '\n' + rec +'\n' + '\n' + 'Сообщение с исправленной ошибкой без дополнительного кода:' +'\n' + re_hamm)
  #file.close()

#print('\n', 'Это все продублировано в файле recevied.txt')
