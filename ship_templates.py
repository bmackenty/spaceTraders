class ShipTemplate:
    def __init__(self, name='default', speed=0, crew=0, x=0, y=0, z=0):
        self.category = 'ship'
        self.name = name
        self.speed = speed
        self.crew = crew
        self.x = x
        self.y = y
        self.z = z
        self.heading = 0
        self.pitch = 0
        self.roll = 0
        self.velocity = speed  # Assuming velocity is related to speed.
        self.sensorContacts = []  # List of objects detected by sensors.
        print(f"Ship '{self.name}' created")

    def update_position(self):
        # Update the position of the ship based on its speed.
        self.x += self.speed
        self.y += self.speed
        self.z += self.speed
        print(f"Ship '{self.name}' position updated: x={self.x}, y={self.y}, z={self.z}")

    def update_orientation(self, heading=0, pitch=0, roll=0):
        # Optional update to orientation.
        self.heading = heading
        self.pitch = pitch
        self.roll = roll
        print(f"Ship '{self.name}' orientation updated: heading={self.heading}, pitch={self.pitch}, roll={self.roll}")

    def detect_objects(self, objects):
        # Simulate detection of objects.
        self.sensorContacts.extend(objects)
        print(f"Ship '{self.name}' detected {len(objects)} objects.")


