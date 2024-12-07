# TODO Напишите функцию find_common_participants
from typing import List
def find_common_participants(participants_first_group,participants_second_group, c=','):
    part_first_group_list = participants_first_group.split(c)
    part_second_group_list = participants_second_group.split(c)
    result = []
    for i in range(len(part_first_group_list)):
        for g in range(len(part_second_group_list)):
            if part_first_group_list[i] == part_second_group_list[g]:
                result.append(part_first_group_list[i])
    result.sort()
    return result

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group,participants_second_group,'|')