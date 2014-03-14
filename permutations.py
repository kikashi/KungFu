def permutations(s):

  if len(s)<=1:
    return [s]

  #get first
  char= s[0]
  #go thru rest
  perms= permutations(s[1:])

  result= []

  for perm in perms:
    for i in range(len(perm)+1):
      result.append(perm[:i]+ char + perm[i:])
  return result

print permutations("abc")
