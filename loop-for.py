#- range for increment (start position, condition (less-than no.), increment by)
#    - range with one parameter: range(5) = range(0, <5, 1) => 0,1,2,3,4 (Start with 0, run till (5-1) with increment of 1)
#    - range with two parameter: range(1, 6) = range(1, <6, 1) => 1,2,3,4,5 (Start with 1, run till (6-1) with increment of 1)
#    - range with three parameter: range(1,6,2) = range(1, <6, 2) => 1,3,5 (Start with 1, run till (6-1) with increment of 2)
# - range for decrement (start position always > than condition number, condition (run till n-1), increment by must be always -1)

for n in range(5):
   print(n)
 
# Python program to create 2's table.

 for a in range(1,11):
   print("2*",a,"=",2*a)
  
 for n in range(10,0,-1):
   print(n)
 #10 9 8 7 6 5 4 3 2 1
  
 for n in range(10,0,-2):
   print(n)
 #10 8 6 4 2 0
