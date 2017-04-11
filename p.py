import sys

class Cars:
  def __init__(self):
    self.makes = list()
    self.models = list()
    self.makes_and_models = dict()

  def read_makes(self):
    with open('car_makes', 'r') as make_file:
      for line in make_file:
        self.makes.append(line[:-1])
    print(self.makes)

  def read_models(self):
    with open('car_models', 'r') as model_file:
      for line in model_file:
        self.models.append(line[:-1])
    print(self.models)

  def get_makes_and_models(self):
    self.read_makes()
    self.read_models()
    for make in self.makes:
      self.makes_and_models[make] = [model[2:] for model in self.models if model[:1].lower() == make[:1].lower()]
    return self.makes_and_models

if __name__ == '__main__':
  c = Cars()
  print(c.get_makes_and_models())