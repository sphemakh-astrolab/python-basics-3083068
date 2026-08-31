# Lab V: A Gentle Introduction to Python
# Programming Essentials for Astronomy I - Python
#
# Fill in the TODOs below. Run this file (no compiling needed!) with:
#     python3 intro_to_python.py

# --- Part A: first steps ---------------------------------------------------

# Exercise 1: Hello, Universe
print("Hello, Universe!")
print("My name is Karabo Mfisa.")
print("My favorite celestial object is Betelgeuss.")
# TODO: also print your name and your favourite celestial object.


# Exercise 2: variables and types
name = "Sirius"           # str
distance_ly = 8.6         # float
num_planets = 0           # int
naked_eye_visible = True  # bool

# TODO: print each variable together with its type, e.g.
#       print(name, "has type", type(name))
print(name,"has type",type(str))
print(distance_ly,"has type",type(float))
print(num_planets,"has type",type(int))
print(naked_eye_visible,"has type",type(bool))

# --- Part B: arithmetic with astronomy -------------------------------------

# Exercise 3: unit conversions (1 parsec ~= 3.26 ly, 1 ly ~= 9.46e12 km)
# TODO: convert distance_ly to parsecs and to kilometres, and print both
#       using f-strings.
distance_pc=distance_ly/3.26
distance_km=distance_ly*9.46e12
print(f"Sirius is {distance_pc} parsecs away.")
print(f"Sirius is {distance_km} km away.")

# Exercise 4: we see the past
# TODO: print the year the light we see now left Sirius (use 2026 as "now").
# TODO: print 8.6 / 3 and 8 // 3 and notice the difference.
print("The light reaching the Earth from Sirius left it in 2017 which is 8.6 years before now.")
print(8.6/3)
print(8//3)

# Exercise 5: the power operator (**) -- volume of a sphere
pi = 3.14159
radius_km = 696000  # the Sun
# TODO: compute volume = (4/3) * pi * radius_km ** 3 and print it with {volume:.3e}
volume = (4/3) * pi * radius_km ** 3 
print(f"The Sun's volume is about {volume:.3e} cubic km")

# --- Part C: talking to the user -------------------------------------------

# Exercise 6: reading input
# NOTE: input() returns TEXT -- convert it with float(...) before doing maths.
# Uncomment the two lines below once you are ready to try it:
# text = input("Enter a distance in light-years: ")
# print(f"That is {float(text) / 3.26:.2f} parsecs.")
text = input("Enter a distance in light-years: distance_ly ")
distance_ly = float(text)   # input() ALWAYS gives text — convert it!
print(f"That is {distance_ly / 3.26:.2f} parsecs.")

# --- Optional extension ----------------------------------------------------
# import math
# TODO: distance modulus  mu = 5 * math.log10(d) - 5  for d in parsecs.
import math
print(math.pi)
print(math.log10(100))
# Lab V: A Gentle Introduction to Python
# Programming Essentials for Astronomy I - Python
#
# Fill in the TODOs below. Run this file (no compiling needed!) with:
#     python3 intro_to_python.py

# --- Part A: first steps ---------------------------------------------------

# Exercise 1: Hello, Universe
print("Hello, Universe!")
# TODO: also print your name and your favourite celestial object.


# Exercise 2: variables and types
name = "Sirius"           # str
distance_ly = 8.6         # float
num_planets = 0           # int
naked_eye_visible = True  # bool

# TODO: print each variable together with its type, e.g.
#       print(name, "has type", type(name))


# --- Part B: arithmetic with astronomy -------------------------------------

# Exercise 3: unit conversions (1 parsec ~= 3.26 ly, 1 ly ~= 9.46e12 km)
# TODO: convert distance_ly to parsecs and to kilometres, and print both
#       using f-strings.

# Exercise 4: we see the past
# TODO: print the year the light we see now left Sirius (use 2026 as "now").
# TODO: print 8.6 / 3 and 8 // 3 and notice the difference.

# Exercise 5: the power operator (**) -- volume of a sphere
pi = 3.14159
radius_km = 696000  # the Sun
# TODO: compute volume = (4/3) * pi * radius_km ** 3 and print it with {volume:.3e}


# --- Part C: talking to the user -------------------------------------------

# Exercise 6: reading input
# NOTE: input() returns TEXT -- convert it with float(...) before doing maths.
# Uncomment the two lines below once you are ready to try it:
# text = input("Enter a distance in light-years: ")
# print(f"That is {float(text) / 3.26:.2f} parsecs.")


# --- Optional extension ----------------------------------------------------
# import math
# TODO: distance modulus  mu = 5 * math.log10(d) - 5  for d in parsecs.
