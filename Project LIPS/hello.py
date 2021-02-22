class web:
    star = "King"
    def sky(self):
        print("sapan")
        print("MCA")

    def prop(self):
        print("water")
        print("black")

class new(web):
    def sky(self):
        print("sonker",super().star)
        print("m-tech")

    def props(self):
        print("pizza")
        print("white")

obj = new()
obj.sky()
