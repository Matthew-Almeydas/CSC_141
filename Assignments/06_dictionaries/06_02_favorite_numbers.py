# Chapter 6 L2
#this program will be a dictionary which stores peoples favorite numbers

favorite_numbers = {'Matthew': 17,
                    'Joe': 67,
                    'Patrick': 42,
                    'Yusef': 21,
                    'Judah': 69}
print(f'(favorite_numbers['Yusef']) is the favorite.')

for key, value in favorite_numbers.items():
    print(f'The key is (key) and the value is (value)')