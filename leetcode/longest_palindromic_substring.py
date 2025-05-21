def solve(s):

  ans = ""
  max_len = 0
  
  record = {}
  for i in range(len(s)):
    record[i] = [i]

  for i in range(1, len(s)):

    if s[i-1] == s[i]:
      record[i].append(i-1)

      if 2 > max_len:
          max_len = 2
          ans = s[i-1:i+1]

    for j in record[i-1]:
      if j-1 >= 0 and s[j-1] == s[i]:
        record[i].append(j-1)
        
        if i-j+2 > max_len:
          max_len = i-j+1
          ans = s[j-1:i+1]
  
  return ans