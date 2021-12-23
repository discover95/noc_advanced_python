
class Nuller():
    owners = dict()

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, owner, value):
        owner.__dict__[self.name] = value
        if owner not in Nuller.owners:
            Nuller.owners[owner] = [self.name]
        else:
            if self.name not in Nuller.owners[owner]:
                Nuller.owners[owner].append(self.name)

    def __get__(self, owner, owner_cls):
        return owner.__dict__[self.name]

    def __delete__(self, owner):
        del owner.__dict__[self.name]
        if len(Nuller.owners[owner]) <= 1:
            Nuller.owners.pop(owner)
        else:
            Nuller.owners[owner].remove(self.name)

    @classmethod
    def null(cls):
        for owner, names in cls.owners.items():
            for name in names:
                owner.__dict__[name] = 0

# use
class Team:
    score = Nuller()
    score1 = Nuller()

print(Nuller.__dict__['owners'])

team1 = Team()
team2 = Team()
team1.score = 5
team1.score1 = 2
print(team1.score, team1.score1)

    # 5

team2.score = 28
print(team2.score)
print(Nuller.__dict__['owners'])

    # 28

Nuller.null()
print(team1.score, team1.score1, team2.score)

    # 0 0

qwe = team1.score

team1.score = 10
print(team2.__dict__, Nuller.__dict__['owners'])
del team2.score
print(team2.__dict__, Nuller.__dict__['owners'])
Nuller.null()
team2.score = 10
print(team2.__dict__, Nuller.__dict__['owners'])
print(team1.score)
    # 0
team3 = Team()
