class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        assert type(name) == str
        assert type(age) == int
        assert type(tracks) == list
        assert type(score) == float

        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, new_name):
        assert type(new_name) == str

        self.name = new_name

    def change_age(self, new_age):
        assert type(new_age) == int

        self.age = new_age

    def add_track(self, new_track):
        assert type(new_track) == str

        self.tracks.append(new_track)

    def get_score(self):
        return self.score

    
    def __repr__(self):
        return f"<Student Name: {self.name} Age: {self.age} Tracks: {self.tracks} Score: {self.score}>"
    




Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(35)
Bob.add_track("UI/UX")
Bob.get_score()

