# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Для этого использовать шаблон template и подставить в него значения из строки
ospf_route. Значения из строки ospf_route надо получить с помощью Python.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0" 
#ospf_route = ospf_route.split()
#ospf_route[1] = ospf_route[1].strip('[]')
#ospf_route[3] = ospf_route[3].strip(',')
#ospf_route[4] = ospf_route[4].strip(',')
#template = """
#Prefix                {0}
#AD/Metric             {1}
#Next-Hop              {2}
#Last update           {3}
#Outbound Interface    {4}
#"""
#print(template.format(ospf_route[0], ospf_route[1], ospf_route[3],ospf_route[4], ospf_route[5]))

template = "\n{:30} {}" * 5
 
ospf_route = ospf_route.replace(',', ' ').replace('[', ' ').replace(']', ' ')
ospf_route = ospf_route.split()
print(template.format(
    'Prefix',ospf_route[0],
    'AD/Metric',ospf_route[1],
    'Next-Hop',ospf_route[3],
    'Last update',ospf_route[4],
    'Outbound Interface',ospf_route[5]
 ))

