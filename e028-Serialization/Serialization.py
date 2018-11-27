try:
    import cPickle as pickle
except ImportError:
    import pickle

animal_list = ["dog", "cat", "frog", "fish"]
binary_file = open("animals", "wb")
pickle.dump(animal_list, binary_file)
binary_file.close()

binary_file = open("animals", "rb")
animal_list = pickle.load(binary_file)
print(animal_list)
