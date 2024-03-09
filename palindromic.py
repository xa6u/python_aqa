print('Enter the string, and I will check is it palindromic')

string = input().lower().replace(" ", "").replace(",", "")
is_palindrome = True

for i in range(len(string) // 2):
    if string[i] != string[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print('This string is a palindrom')
else:
    print('This string is  NOT a palindrom')