
# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

mac = "AAAA:BBBB:CCCC"
#string_a=mac.split(":")
#string_a1=list(string_a[0])
#string_a2=list(string_a[1])
#string_a3=list(string_a[2])
#A=10
#B=11
#C=12
#string_a1[0]=A
#string_a1[1]=A
#string_a1[2]=A
#string_a1[3]=A
#string_a2[0]=B
#string_a2[1]=B
#string_a2[2]=B
#string_a2[3]=B
#string_a3[0]=C
#string_a3[1]=C
#string_a3[2]=C
#string_a3[3]=C
#template = "{:b}" * 12
#print (template.format((string_a1[0]), (string_a1[1]), (string_a1[2]), (string_a1[3]), (string_a2[0]), (string_a2[1]), (string_a2[2]), (string_a2[3]), (string_a3[0]), (string_a3[1]), (string_a3[2]), (string_a3[3]) ))

print ("{:b}".format(int(mac.replace(":",""), 16)))

