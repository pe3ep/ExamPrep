from itertools import *
print(len([i for i in list(product("ABCDXY", repeat=4)) if ( i[0] == "X" and i.count("X") == 1 and i.count("Y") == 0 ) or ( i[0] == "Y" and i.count("Y") == 1 and i.count("X") == 0 )]))


print(2*len(list(product("ABCD", repeat=3))))