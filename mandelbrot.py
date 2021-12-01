import numpy
import colorsys

from math import sqrt
from PIL import Image

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other): return Complex(self.r + other.r, self.i + other.i)
    def __sub__(self, other): return Complex(self.r - other.r, self.i - other.i)
    def __mul__(self, other): return Complex(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)
    def __truediv__(self, other): return Complex((self.r * other.r + self.i * other.i) / (other.r * other.r + other.i * other.i), (self.i * other.r - self.r * other.i) / (other.r * other.r + other.i * other.i))
    def __neg__(self): return Complex(-self.r, -self.i)
    def __len__(self): return sqrt(self.r * self.r + self.i * self.i)
    def __repr__(self): return f"({self.r} + {self.i}i)"
    @property
    def magnitude(self): return self.__len__()

i = Complex(0, 1)

def mandelbrot(c, max_steps): return mandelbrot_recursive(c, c, max_steps, 0)
def mandelbrot_recursive(z, c, max_steps, step):
    if step == max_steps or z.magnitude > 2: return step
    z = z * z + c
    return mandelbrot_recursive(z, c, max_steps, step + 1)

max_steps = 50
size = 1000
imageData = numpy.zeros((size, size, 3), dtype=numpy.uint8)
for y in range(size):
    print(y)
    for x in range(size):
        if y > size / 2: 
            imageData[y, x] = imageData[size - y, x]
        else:
            c = Complex(4 * x / size - 2, 4 * y / size - 2)
            steps = mandelbrot(c, max_steps)
            if steps == max_steps:
                imageData[y, x] = [0, 0, 0]
            else:
                v = 255 - steps / max_steps * 255
                imageData[y, x] = [v, v, v]

image = Image.fromarray(imageData)
image.show()
