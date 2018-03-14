class Area:

    def __init__(self, width, height, objects = [], characters = []):
        self.width = width
        self.height = height
        self.objects = objects
        self.characters = characters

    def find_character_by_name(self, name):
        for c in self.characters:
            if c.name.lower() == name.lower():
                return c

    def delete_object():
        print("Not implemented!")
