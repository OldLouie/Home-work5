immutable_var = 2, 5, 'aplle', 'banana'
#immutable_var[0][0] = 9
#immutable_var.extend(['modified'])
print(immutable_var)
# Кортежи неизменяемы. Это значит, что элементы кортежа нельзя изменять после добавления в кортеж.
# Однако если элемент сам по себе является изменяемым типом данных (например, списком),
# его вложенные элементы менять уже можно, как показано во втором варианте.
mutable_list = [[2, 5], 'apple', 'banana',]
mutable_list.extend(['Modified'])
mutable_list[0][1] = 9
print(mutable_list)