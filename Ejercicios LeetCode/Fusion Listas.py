class Solution(object):
    def mergeTwoLists(self, list1, list2):
        listAct = sorted(list1 +list2)
        return listAct
    
entrada1 = input('1. Introduzca los valores separados por comas: ')
entrada2 =input('2. Introduzca los valores separados por comas: ')

list1 = [elemento.strip() for elemento in entrada1.split(',')]
list2 = [elemento.strip() for elemento in entrada2.split(',')]


sol = Solution()
print(sol.mergeTwoLists(list1,list2))    