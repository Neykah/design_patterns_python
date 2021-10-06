from dataclasses import dataclass
from abc import ABC, abstractmethod

####################################
#### Dependency and Association ####
####################################

class Student:
    def remember(self):
        ...


class Course:
    def get_knowledge(self):
        ...


@dataclass
class Professor:
    student: Student

    def teach(self, course: Course):
        ...
        self.student.remember(course.get_knowledge())

#####################################
#### Aggregation and Composition ####
#####################################

class Department:
    def __init__(self, name: str, professors: list[Professor]):
        """
        Departments contains professors.
        Professors still exists if the Department is dissolved.
        """
        self.professors = professors


class University:
    def __init__(self):
        """
        University consists in Departments.
        Departments do not exist outside of University.
        If University is deleted, the Departments are also deleted.
        """
        self.departments = [
            Department(name, [])
            for name in ["Science", "Computer Science", "Art"]
        ]


########################################
#### Implementation and Inheritance ####
########################################

@dataclass
class Animal:
    age: int
    name: str
    position: float

    def move(self, speed: float, duration: float = 1.0) -> None:
        self.position += speed * duration

class FourLegged(ABC):
    @abstractmethod
    def run(self, destination: str) -> None:
        ...

@dataclass
class OxygenBreather(ABC):
    nb_lungs: int
    @abstractmethod
    def breath(self):
        ...

class Cat(Animal, FourLegged, OxygenBreather):
    def run(self, destination: str) -> None:
        # ! MANDATORY
        self.move(30)
        ...

    def breath(self) -> None:
        # ! MANDATORY
        print("Inhale...")
        print("EXHALE!!!")

