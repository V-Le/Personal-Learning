elements = {"hydrogen": {"number": {"test1": 44,    # adding a list within a list within a list
                                    "test2": 33},
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

hydrogen = elements["hydrogen"]  # get the hydrogen dictionary
elements["hydrogen"]["number"]["test3"] = 95    # adding a new key:value to hydrogen > number

print(elements["hydrogen"]["number"])

oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)
