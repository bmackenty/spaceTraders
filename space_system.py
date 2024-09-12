class SpaceSystem:
    def __init__(self):
        self.x = 1000
        self.y = 1000
        self.z = 1000
        self.objects = []
        print('SpaceSystem created')
    
    def add_object(self, object):
        self.objects.append(object)
    
    # show current objects in the system
    def show_objects(self):
        for object in self.objects:
            print(object.name)
    
    # update all the objects in the system
    def update(self):
        for object in self.objects:
            object.update_position()
            object.update_orientation()
            object.detect_objects(self.objects)

    
    def remove_object(self, object):
        self.objects.remove(object)
        print(f"Object '{object.name}' removed from system.")
    
    # get the distance between two objects
    def get_distance(self, object1, object2):
        distance = ((object1.x - object2.x)**2 + (object1.y - object2.y)**2 + (object1.z - object2.z)**2)**0.5
        return distance
