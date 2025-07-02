#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    res = "Hello " + first + " " + last + "! You just delved into python."
    print(res)

if __name__ == '__main__':
    first_name = input("FirstName : ")
    last_name = input("LastName :")
    print_full_name(first_name, last_name)