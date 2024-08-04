import os

for i in range(43, 51):
    str_i = str(i)
    end_str_i = str(i)
    if i < 10:
        end_str_i = '0' + str_i
    os.rename("problem{}.py".format(str_i), "P{}.py".format(end_str_i))