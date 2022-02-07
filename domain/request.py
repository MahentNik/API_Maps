class Request:
    def __init__(self):
        self.longitude = 37.530887
        self.latitude = 55.703118
        self.zoom = 15
        self.type = 'map'

    def get_longitude(self):
        return self.longitude

    def get_latitude(self):
        return self.latitude

    def get_zoom(self):
        return self.zoom

    def get_type(self):
        return self.type

    def zoom_up(self):
        if self.zoom < 17:
            self.zoom += 1

    def zoom_down(self):
        if self.zoom > 0:
            self.zoom -= 1
