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
            object.update()
