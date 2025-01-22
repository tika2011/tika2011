#clasework1
def double_list_elements(num_list):
    num_list =[]
    for i in num_list:
        num_list.append(i*2)
    return num_list
print(double_list_elements([ 2, 3, 4, 6, 8, 9]))

#clasework2
def add_item(item_list, item):
  #  item_list,append(item)
    return item_list
print(add_item([1, 2, 3,],4))

#clasework3
def remove_item(item_list, item):
  #  item_list,remove(item)
    return item_list
print(remove_item([1,2, 3, 4, ], 3))

#clasework4
def min_item(num_list):
    minin_list = num_list[0]
    for i in num_list:
        if i < minin_list:
            minin_list = 1
            return minin_list
        print(min_item([8, 9, 123, 40, 5, 2, 1000]))