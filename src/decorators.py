
def argument_check(*types_args,**types_kwargs):
    """
    INFORMATION: Standard decorator with arguments that is used to verify the agument (arg) or opttion arguments (kwargs) 
                 of linked function. If the decorator see an not valid argument or kwarg in the funcion. 
                 There will be generate an exception with the explanation with the argument that is not correct.
    INPUT: 
        - *types_args: Tuple of arguments where eatch argument can will be a a type (simple object type) or types of 
                       object types (when you define a tuple of objects). Or if it is defined as an list. Those values of the list 
                       are the option of the values thay those arguments can will be.
        - **types_kwargs: dict of kwargs where eatch argument can will be a a type (simple object type) or types of object types 
                          (when you define a tuple of objects). Or if it is defined as an list for a key of a dict. The keyvalue of a
                          dict must be in the defined list liked to that veyvalue.
    OUTPUT:
        - ERROR: EXECUTION OF THE LINKED FUNCTION
        - NO ERROR: A DEFINED EXCEPTION

    """
    def check_accepts(f):
        def function_wrapper(*args, **kwargs):
            assert len(args) is len(types_args), f"In function '{f.__name__}{args}' and option values: {kwargs}, lenght of argumnets {args} is not the same as types_args {types_args}"
            for (arg, type_arg) in zip(args, types_args):
                if isinstance(type_arg,list):
                    assert arg in type_arg, f"In function '{f.__name__}{args}' and option values: {kwargs}, argument {arg} is not in list {type_arg}" 
                else:
                    assert isinstance(arg, type_arg), f"In function '{f.__name__}{args}' and option values: {kwargs}, arg {arg} does not match {type_arg}" 
            for kwarg,value in kwargs.items():
                assert kwarg in types_kwargs , f"In function '{f.__name__}{args}' and option values: {kwargs}, the kwarg ('{kwarg}':{value}) is not a valid option value" 
                espected_format = types_kwargs[kwarg]
                if isinstance(espected_format,list): 
                    assert value in espected_format, f"In function '{f.__name__}{args}' and option values: {kwargs}, the kwarg value ('{kwarg}':{value}) is not in list {espected_format}" 
                else:
                    assert isinstance(value, espected_format), f"In function '{f.__name__}{args}' and option values: {kwargs}, kwarg value ('{kwarg}':{value}) does not match with {espected_format}" 
            return f(*args, **kwargs)
        function_wrapper.__name__ = f.__name__
        return function_wrapper
    return check_accepts 