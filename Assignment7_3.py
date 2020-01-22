import math;
class Numbers:
	def __init__(self,val):
		self.value = val
		
	def ChkPrime(self):
		if (self.value==1):
			return False
		elif (self.value==2):
			return True;
		else:
			for x in range(2,self.value):
				if(self.value % x==0):
					return False
			return True 
		
	def ChkPerfect(self):
		sum=0;
		for i in range(1,self.value):
			if(self.value%i==0):
				sum+=i
		if(sum==self.value):
			return True
		else:
			return False
	
	def SumFactor(self):
		result=0
		for i in range(2,(int)(math.sqrt(self.value))+1):
			if(self.value%i==0):
				if(i==(self.value/i)):
					result+=i;
				else:
					result=result+(i+self.value//i)
		return(result+self.value+1)
	

def main():
        
	no=int(input("Enter The Number:"))
	obj1 = Numbers(no)
	true=1;
	a=obj1.ChkPrime();
	if a==true:
	    print("the no is prime")
	else:
            print("the no is not prime")
	b=obj1.ChkPerfect();
	if b==true:
	    print("the no is perfect")
	else:
	    print("the no is not perfect")
	c=obj1.SumFactor();
	print("the addition of factors is",c)
	
if __name__=="__main__":
	main();