import traceback
from wsgiref.simple_server import make_server

"""
For your homework this week, you'll be creating a wsgi application of
your own.

You'll create an online calculator that can perform several operations.

You'll need to support:

  * Addition
  * Subtractions
  * Multiplication
  * Division

Your users should be able to send appropriate requests and get back
proper responses. For example, if I open a browser to your wsgi
application at `http://localhost:8080/multiple/3/5' then the response
body in my browser should be `15`.

Consider the following URL/Response body pairs as tests:

```
  http://localhost:8080/multiply/3/5   => 15
  http://localhost:8080/add/23/42      => 65
  http://localhost:8080/subtract/23/42 => -19
  http://localhost:8080/divide/22/11   => 2
  http://localhost:8080/               => <html>Here's how to use this page...</html>
```

To submit your homework:

  * Fork this repository (Session03).
  * Edit this file to meet the homework requirements.
  * Your script should be runnable using `$ python calculator.py`
  * When the script is running, I should be able to view your
    application in my browser.
  * I should also be able to see a home page (http://localhost:8080/)
    that explains how to perform calculations.
  * Commit and push your changes to your fork.
  * Submit a link to your Session03 fork repository!


"""


def add(*args):
    """ Returns a STRING with the sum of the arguments """

    # TODO: Fill sum with the correct value, based on the
    # args provided.
    nums = [int(i) for i in args]
    total = sum(nums)
    # for arg in args:
      # int(summ) + int(arg)
    return str(total)

def subtract(*args):
    """ Returns a STRING with the sum of the arguments """

    # TODO: Fill sum with the correct value, based on the
    # args provided.
    # sub = "0"
    nums = [int(i) for i in args]
    total = nums.pop(0)
    for n in nums:
      total = total - n
    return str(total)

def multiply(*args):
    """ Returns a STRING with the sum of the arguments """

    # TODO: Fill sum with the correct value, based on the
    # args provided.
    # product = "0"
    nums = [int(i) for i in args]
    total = nums.pop(0)
    for n in nums:
      total = total * n
    return str(total)

    return product

def divide(*args):
    """ Returns a STRING with the sum of the arguments """

    # TODO: Fill sum with the correct value, based on the
    # args provided.
    # div = "0"
    nums = [int(i) for i in args]
    total = nums.pop(0)
    for n in nums:
      total = total/float(n)
    return str(total)

    return div

# TODO: Add functions for handling more arithmetic operations.

def resolve_path(path):
    """
    Should return two values: a callable and an iterable of
    arguments.
    """

    # TODO: Provide correct values for func and args. The
    # examples provide the correct *syntax*, but you should
    # determine the actual values of func and args using the
    # path.

    # path is something like '/add/3/5'
    # or '/multiply/2/10'

    routes = {
      'add': add,
      'subtract': subtract,
      'multiply': multiply,
      'divide': divide,
    }

    path = path.strip('/').split('/')
    func_name = path.pop(0)
    func = routes.get(func_name)
    if func is None:
      raise NameError
    args = path
    # args = ['25', '32']

    return func, args

def application(environ, start_response):
    headers = [("Content-type", "text/html")]
    try:
        path = environ.get('PATH_INFO', None)
        # path looks like maybe '/add/3/5'
        if path is None:
            raise NameError
        func, args = resolve_path(path)
        body = func(*args)
        status = "200 OK"
    except NameError:
        status = "404 Not Found"
        body = "<h1>Not Found</h1>"
    except Exception:
        status = "500 Internal Server Error"
        body = "<h1>Internal Server Error</h1>"
        print(traceback.format_exc())
    finally:
        headers.append(('Content-length', str(len(body))))
        start_response(status, headers)
        return [body.encode('utf8')]
    # TODO: Your application code from the book database
    # work here as well! Remember that your application must
    # invoke start_response(status, headers) and also return
    # the body of the response in BYTE encoding.
    #
    # TODO (bonus): Add error handling for a user attempting
    # to divide by zero.
    # pass

if __name__ == '__main__':

    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
    # TODO: Insert the same boilerplate wsgiref simple
    # server creation that you used in the book database.
    # pass
