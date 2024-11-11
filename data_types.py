# Creating variables of each primitive data type
my_int1 = 10
my_int2 = 20
my_float1 = 15.5
my_float2 = 3.7
my_str1 = "Hello"
my_str2 = "World"
my_bool1 = True
my_bool2 = False

# Performing arithmetic operations
int_sum = my_int1 + my_int2
float_sum = my_float1 + my_float2
int_product = my_int1 * my_int2
float_product = my_float1 * my_float2

# Performing string concatenation
string_concat = my_str1 + " " + my_str2

# Performing logical operations
bool_and = my_bool1 and my_bool2
bool_or = my_bool1 or my_bool2

# Storing variables in a dictionary by type
data_dict = {
    "int": [my_int1, my_int2, int_sum, int_product],
    "float": [my_float1, my_float2, float_sum, float_product],
    "str": [my_str1, my_str2, string_concat],
    "bool": [my_bool1, my_bool2, bool_and, bool_or]
}

# Displaying the dictionary
for data_type, values in data_dict.items():
    print(f"{data_type}: {values}")
