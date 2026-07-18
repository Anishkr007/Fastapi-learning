from dataclasses import dataclass

@dataclass 
class student:
    name: str
    age: int


student1=student("anish",22)

print(student1.name);
print(student1.age);

@dataclass
class Car:
    brand: str
    price: int

car = Car("BMW", 5000000)

print(car)



@dataclass
class Student:
    name: str
    age: int = 18

s = Student("Anish")

print(s)


@dataclass
class Rectangle:
    length: int
    width: int

    def area(self) -> int:
        return self.length * self.width

r = Rectangle(10, 5)

print(r.area())