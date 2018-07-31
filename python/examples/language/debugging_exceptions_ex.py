import traceback

try:
    raise Exception('Error Message')
except:
    errorFile = open('C:\\temp\\error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Traceback written to error_log.txt')

assert False, 'This is the error message.'

market_2nd = {'ns': 'green', 'ew': 'red'}


def switch_lights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red' + str(intersection)

switch_lights(market_2nd)

# We can use three methods to handle multiple exceptions.
# The first one involves putting all the exceptions which are likely to occur in a tuple.
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("An error occurred. {}".format(e.args[-1]))

# Another method is to handle individual exceptions in separate except blocks.
# We can have as many except blocks as we want.
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    raise e
except IOError as e:
    print("An error occurred.")
    raise e

# This way if the exception is not handled by the first except block
# then it may be handled by a following block, or none at all.
try:
    file = open('test.txt', 'rb')
except Exception:
    # Some logging if you want
    raise


try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")

