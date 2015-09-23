
def example1():
    '''simple decorator'''
    def simple_decorator(function):
        print "doing decoration"
        return function
    
    @simple_decorator
    def function():
        print "inside function"
        
    function()

# example1()

def example2():
    def decorator_with_arguments(arg):
        print "defining the decorator"
        def _decorator(function):
            # in this inner function, arg is available too
            print "doing decoration,", arg
            return function
        return _decorator
    
    @decorator_with_arguments("abc")
    def function():
        print "inside function"
        
    function()
example2()