start = input("Enter value:")
end = input("Enter value:")
    
d = {}
for i in range(ord(start), ord(end)+1):
      d[chr(i)]=i
    
print(d)


               
