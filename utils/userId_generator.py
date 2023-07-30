import random

def generate_random_string(length):
  """Generates a random string of the specified length."""
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  random_string = ""
  for _ in range(length):
    random_index = random.randrange(len(characters))
    random_character = characters[random_index]
    random_string += random_character
  return random_string

if __name__ == "__main__":
  random_string = generate_random_string(10)
  print(random_string)
