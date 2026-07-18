age : int = 22;

print(age);

marks:float=22.22;

print(marks);

name: str = "Anish";

print(name);

is_hero : bool= False;

print(is_hero);

def square(x:int)->int:
    return x*x;


a:int=square(34);
print(a);

def introduce(name: str, age: int) -> str:
    return f"My name is {name}. I am {age} years old."

print(introduce("Anish", 22))

def average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)

print(average([90, 80, 70]))

def add(a: int, b: int):
    return a + b

print(add("10", "20"))