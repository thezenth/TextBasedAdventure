class Area:

    def __init__(self, name, width, height, objects = [], characters = []):
        self.name = name
        self.width = width
        self.height = height
        self.objects = objects
        self.characters = characters

    def find_character_by_name(self, name):
        for c in self.characters:
            if c.name.lower() == name.lower():
                return c

    def check_if_object_at_position(self, x, y):
        for o in self.objects:
            if (o.x == x and o.y == y):
                return o

        for c in self.characters:
            if (c.x == x and c.y == y):
                return c

        return None

    def print_area_map(self):
        mapStr = ""

        for y in range(0, self.width + 1):
            for x in range(0, self.height + 1):
                obj = self.check_if_object_at_position(x, y)
                if obj is not None:
                    mapStr += obj.char
                else:
                    mapStr += "."

                mapStr += ""
            mapStr += "\n"

        return mapStr

    def delete_object():
        print("Not implemented!")
