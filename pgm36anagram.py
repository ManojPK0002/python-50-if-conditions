'''Given two strings, write a program to determine whether they are
anagrams.'''
str1=input("Enter the string1").lower()
str2=input("Enter the string2").lower()

if(len(str1)!=len(str2)):
    print("The strings are not an anagram")
else:
    if sorted(str1)==sorted(str2):
        print(f"{str1} and {str2} strings are anagram")
    else:
        print(f"{str1} and {str2} strings are not anagram")