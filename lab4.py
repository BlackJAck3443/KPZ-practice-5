import platform
import ipaddress
import pytest

# завдання 1
def prime_num_generator():
    for n in range(2, 1000):  
        for x in range(2, n):  
            if n % x == 0:  
                break
        else: 
            yield n
        n += 1

a = prime_num_generator()

b = prime_num_generator()
i = 0;
needed_num = 0;

while(i <= 101):
    needed_num = next(b)
    print(needed_num)
    i = i + 1
    @pytest.mark.parametrize("expected_result", [4, 5, 8, 9, 12, 15, 17, 18, 25, 27, 33, 35])
def test_prime_num_generator(expected_result):
    assert next(a) == expected_result

@pytest.mark.parametrize("expected_result", [455])
def test_prime_num_generator_2(expected_result):
    assert needed_num == expected_result

# завдання 2

def palindrome(text):

    word_list = []
    temp = ''
    for i, v in enumerate(text):
        if v.isalpha():  
            temp += v
            if i == len(text) - 1 and temp.isalpha():
                word_list.append(temp)  
        else: 
            word_list.append(temp)
            temp = ''



    pal_words = []
    for i in word_list:
        reversed_word = i[::-1]  
        if len(i) < 3:
            break
        if reversed_word == i: 
            pal_words.append(i)
    return pal_words


@pytest.mark.parametrize("palindrome_func_arg, result", [("add", []), ("adda", ["adda"]), ("ada", ["ada"]), (5, [])])
def test_palindrome(palindrome_func_arg, result):
    try:
        assert palindrome_func_arg != ''
        assert palindrome(palindrome_func_arg) == result
    except TypeError:
        print()
        print()
        print("Неправильний аргумент: int - недійсний тип аргументу")


    
# завдання 3

def validate_ip(ip_address):
   ip_validate = False
   try:
      ip = ipaddress.ip_address(ip_address)
      ip_validate = True
   except ValueError:
      ip_validate = False

   return ip_validate




@pytest.mark.parametrize("validate_ip_func_arg, result", [("192.168", False), ("-1.168.1.30", False),
                                                          ("192.200.1.30", False),
                                                          ("192.168.-34.32", False),
                                                          ("192.168.1.320", False)])
def test_validate_ip(validate_ip_func_arg, result):
    assert validate_ip_func_arg != ''
    assert validate_ip(validate_ip_func_arg) == result

# завдання 4
def get_os():
   return platform.system()


def test_get_os():
   assert get_os() == "Windows"

