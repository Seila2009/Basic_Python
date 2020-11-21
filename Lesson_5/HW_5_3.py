with open('staff.txt', 'r', encoding='utf-8') as f_obj:
    i = 0
    for line in f_obj:
        staff, payday = line.split()
        i += float(payday)
        if float(payday) <= 20000:
            print(f'Зарплата меньше 20.000 у {staff}')
av_payday = i / len(staff)
print(f'средний оклад {av_payday}')
