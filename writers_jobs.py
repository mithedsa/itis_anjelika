import datetime
from abc import ABC, abstractmethod

class Writer:
    def __init__(self, birsth: datetime.date, death: datetime.date, name: str, sername: str, nick: str, country: str, add_job, works: list, ):
        self.birsth = birsth
        self.death = None
        self.name = name
        self.sername = sername
        self.nick = nick
        self.country = country
        self.add_job = add_job
        self.works = works

class Publish():
    def __init__(self, address, director, year_of_foundation):
        self.adress = address
        self.director = director
        self.year_of_foundation = year_of_foundation

class Work(Writer):
    def __init__(self, writers, publish):
        self.writers = [Writer()]
        self.publih = [Publish()]

def add_autor():
    autor = Work()
    return autor

class Book(Work):
    def __init__(self, binding, cover):
        self.binding = binding
        self.cover = cover

class Magazine(Work):
    def __init__(self, cover_type):
        self.cover_type = cover_type

class Publication(Work):
    def __init__(self, place_of_publication):
        self.place = place_of_publication
