def say_hi(name, age):
  return f"HI, My name is {name} and I'm {age} years old"

assert say_hi("Alex", 32) == "HI, My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "HI, My name is Frank and I'm 68 years old", 'Test2'

print('OK')