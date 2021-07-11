a = [10, 20, 30,40, 20, 10, 50, 60, 40, 80, 50,50, 40]

dup_items = set()
uniq_items = []
for x in a:
  if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
print(dup_items)


'''
task1 is check the duplicate name from the list


'''
