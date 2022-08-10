import pyglet


class Camera:

    def __init__(self, scroll_speed=1, min_zoom=1, max_zoom=4):
        assert min_zoom <= max_zoom, "Minimum zoom must not be greater than maximum zoom"
        self.scroll_speed = scroll_speed
        self.max_zoom = max_zoom
        self.min_zoom = min_zoom
        self.offset_x = 0
        self.offset_y = 0
        self._zoom = max(min(1, self.max_zoom), self.min_zoom)

    @property
    def zoom(self):
        return self._zoom

    @zoom.setter
    def zoom(self, value):
        self._zoom = max(min(value, self.max_zoom), self.min_zoom)

    @property
    def position(self):
        return self.offset_x, self.offset_y

    @position.setter
    def position(self, value):
        self.offset_x, self.offset_y = value

    def move(self, axis_x, axis_y):
        self.offset_x += self.scroll_speed * axis_x
        self.offset_y += self.scroll_speed * axis_y

    def begin(self):
        pyglet.gl.glTranslatef(-self.offset_x * self._zoom, -self.offset_y * self._zoom, 0)

        pyglet.gl.glScalef(self._zoom, self._zoom, 1)

    def end(self):
        pyglet.gl.glScalef(1 / self._zoom, 1 / self._zoom, 1)

        pyglet.gl.glTranslatef(self.offset_x * self._zoom, self.offset_y * self._zoom, 0)

    def __enter__(self):
        self.begin()

    def __exit__(self, exception_type, exception_value, traceback):
        self.end()


class CenteredCamera(Camera):

    def __init__(self, window: pyglet.window.Window, *args, **kwargs):
        self.window = window
        super().__init__(*args, **kwargs)

    def begin(self):
        x = -self.window.width//2/self._zoom + self.offset_x
        y = -self.window.height//2/self._zoom + self.offset_y

        pyglet.gl.glTranslatef(-x * self._zoom, -y * self._zoom, 0)

        pyglet.gl.glScalef(self._zoom, self._zoom, 1)

    def end(self):
        x = -self.window.width//2/self._zoom + self.offset_x
        y = -self.window.height//2/self._zoom + self.offset_y

        pyglet.gl.glScalef(1 / self._zoom, 1 / self._zoom, 1)

        pyglet.gl.glTranslatef(x * self._zoom, y * self._zoom, 0)

