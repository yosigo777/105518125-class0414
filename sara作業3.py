n = 0
for i in range(1,5):
         for j in range(1,5):
             for k in range(1,5):
                if (i != k) and (i != j) and (j != k):
                   n += 1
                   print(str(i)+str(j)+str(k))

print("總共有{}個互不相同且無重複數字的3位數".format(n))