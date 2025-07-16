my_set = {1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 8, 9, 0}
my_set.add(10)               # Yeni element əlavə etmək
my_set.remove(0)             # Element Silmək 
print(my_set)                # {1, 2, 3, 4, 5, 6, 7, 8, 9} təkrar olunan rəqəmlərdən 1 dənəsi yazılır !


a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))     # {2, 3} ortaq ədədlər seçilir

print(a.union(b))            # {1, 2, 3, 4} Ardıcıl sıra ilə birləşirlər

print(a.difference(b))       # {1} A kataloqunda Olub, B kataloqunda Olmuyanı Tapır

print(b.difference(a))       # {4} B kataloqunda Olub, A kataloqunda Olmuyanı Tapır


my_tuple = (1, 2, 3, 4, 5, 6)

print(my_tuple[1:5])
print(my_tuple[::-1])