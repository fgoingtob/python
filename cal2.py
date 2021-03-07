def add(x, y):
	return x+y;	

def sub(x,y):
	return x - y;

def mul(x, y):
	return x * y;

def div(x, y):
	return x / y;

print("Operation to perform:");
print("1. Addition");
print("2. Subtraction");
print("3. Multiplication");
print("4. Division");

cho = input("select some: ");

num1 = int(input("enter first number: "));
num2 = int(input("enter second number: "));

if cho == '1':
	print(num1, "+", num2, "=", add(num1, num2));

elif cho == '2':
	print(num1, "-", num2, "=", sub(num1, num2));

elif cho == '3':
	print(num1, "*", num2, "=", mul(num1, num2));

elif cho == '4':
	print(num1, "/", num2, "=", div(num1, num2));

else:
	print("mushkil he ah");


