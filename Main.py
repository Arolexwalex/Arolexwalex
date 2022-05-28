```
def find_anagram(str1, str2):
     # [assignment] Add your code here
 
     if(sorted(str1) == sorted(str2)):
         print("Anagrams")
         return True 
     else:
         print("Not Anagrams")
         return False

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

find_anagram(str1, str2)
```
