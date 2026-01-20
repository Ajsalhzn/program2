from collections import UserList

class UniqueList(UserList): 
    def remove_duplicates(self):
        seen = set()
        unique_items = []
        for item in self.data:
            if item not in seen:
                unique_items.append(item)
                seen.add(item)
        self.data = unique_items

my_list = UniqueList([1,2,2,3,4,3,5,1])
print("Original list:", my_list)

my_list.remove_duplicates()
print("After removing duplicates:", my_list)
