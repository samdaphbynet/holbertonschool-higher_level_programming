#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try:
            divided = my_list_1[i]
            divisor = my_list_2[i]
            if not isinstance(divided, (int, float)):
                raise TypeError("wrong type")
            if not isinstance(divisor, (int, float)):
                raise TypeError("wrong type")
            if divisor == 0:
                raise ZeroDivisionError("divition by 0")
            div = divided / divisor
        except IndexError:
            print("out of range")
            div = 0
        except (TypeError, ZeroDivisionError) as error:
            print(str(error))
            div = 0
        finally:
            res.append(div)
    return res
