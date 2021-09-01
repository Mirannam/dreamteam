num =[4311,4321,5542,5631,9871]
for n in num:
	def check(n):
    		p=n%10
    		n=n//10
    		while(n>0):
        		c=n%10
        		if c<p:
            			return False
        		p=c
        		n=n//10
    		return True
    
	print(check(n))


