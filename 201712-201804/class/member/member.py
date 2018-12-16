class Member:

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def out_member(self):
        return self.name + self.age + self.job