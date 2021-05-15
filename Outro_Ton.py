import sys
from PIL import Image, ImageFilter


if __name__ == "__main__":
  print(f'argumentos: {len(sys.argv)}')
  for i, arg in enumerate(sys.argv):
    if i == 1:
      imagen1 = arg
    imagen2 = arg
    print(f"argument {i}: {arg}")


original = open (sys.argv[1], )
transform = open (sys.argv[2],)

CONTOUR = Image.open(imagen1)

CONTOUR1 = CONTOUR.filter(ImageFilter.CONTOUR)


original.close()
saida = CONTOUR1.save(imagen2)

