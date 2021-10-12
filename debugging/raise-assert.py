import traceback

'''
You can raise your own exceptions: raise Exception(‘This is the error message.')
You can also use assertions: assert condition, ‘Error message'
Assertions are for detecting programmer errors that are not meant to be recovered from. User errors should raise exceptions.
'''

"""
**********
*        *
*        *
*        *
*        *
**********

"""


def box_print(symbol: str, width: int, height: int):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a strings of length 1.')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal to 2.')

    print(symbol.rjust(width, symbol))
    for i in range(height):
        print(symbol.ljust(width - 1, ' ') + symbol)
    print(symbol.rjust(width, symbol))


box_print('*', 10, 4)
# box_print('$$', 8, 10)
# box_print('*', 2, 1)

# try:
#     raise Exception('This is an error message')
# except:
#     errorfile = open('error_log.txt', 'a')
#     errorfile.write(traceback.format_exc())
#     errorfile.close()
#     print('The traceback info was written to error_log.txt')

# assert False, 'This is the error message'

market_2nd = {'ns': 'green', 'ew': 'red'}


def switch_lights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)


print(market_2nd)
switch_lights(market_2nd)
print(market_2nd)
