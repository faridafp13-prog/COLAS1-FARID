class Cola:

  def __init__(self):
    self.items = []

  def esta_vacia(self):
    return len(self.items) == 0

  def encolar(self, item):
    self.items.append(item)

  def desencolar(self):
    if not self.esta_vacia():
      return self.items.pop(0)
    return None

  def tamaño(self):
    return len(self.items)


def sumar_colas(cola_a, cola_b):
  cola_resultado = Cola()
  items_a = list(cola_a.items)
  items_b = list(cola_b.items)

  for a, b in zip(items_a, items_b):
    cola_resultado.encolar(a + b)

  return cola_resultado


if __name__ == "__main__":
  # Creación y llenado de Cola A
  cola_a = Cola()
  for num in [3, 4, 2, 8, 12]:
    cola_a.encolar(num)

  # Creación y llenado de Cola B
  cola_b = Cola()
  for num in [6, 2, 9, 11, 3]:
    cola_b.encolar(num)

  # Obtenemos la Cola Resultado
  cola_res = sumar_colas(cola_a, cola_b)

  print("Cola A:", cola_a.items)
  print("Cola B:", cola_b.items)
  print("Cola Resultado (Suma):", cola_res.items)