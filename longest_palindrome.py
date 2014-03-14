def is_palindrome(s):
  return s==s[::-1]

def longest_palindrome(s):
  
  max_pal= ""
  
  for i in range(len(s)):
    for j in range(i+1, len(s)+1):
      sub_str= s[i:j]
      if is_palindrome(sub_str):
        if len(sub_str)> len(max_pal):
          max_pal=sub_str
  return max_pal

print longest_palindrome("racecars")