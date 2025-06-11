def lcp(strs):
    ans = ""

    strs.sort(key=len)

    for i in range(len(strs[0])):
          for str in strs[1:]:
              if str[:i+1] == strs[0][:i+1]:
                  ans = str[:i+1]
              else:
                  return ans
    return ans