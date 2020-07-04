# Import enlarge and invoke enlarge
# Do not import the entire script (if __name__ == "__main__"...)


# from my_mod import enlarge

# Sometimes you may need this
# Will need an init file AND
# Run as '''python -m my_lambdata.hello''' (modular approach)
from my_lambdata.my_mod import enlarge


print('HELLO!')

print(enlarge(10))
