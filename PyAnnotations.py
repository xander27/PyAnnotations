from inspect import isfunction

annotations_to_funcs = {}
func_to_annotations = {}

def get_annotaions(func):
    """
    Get list of annotations for current object
    """
    #There func must be actually anntotaion object
    #So, if it was annotated isfunction = 'false'
    if isfunction(func):
        return []

    #Check is it annotaion
    if hasattr(func, "_Annotation__func"):
        func_key = func._Annotation__func
        if  func_key in func_to_annotations:
            return func_to_annotations[func_key]

    return  []


class Annotation(object):
    """
    Base class for annotations
    """

    def __init__(self, func, *args, **kwargs):
        self.__func = func
        cls = self.__class__

        if not cls in annotations_to_funcs:
            annotations_to_funcs[cls] = []
        annotations_to_funcs[cls].append(func)

        if not func in func_to_annotations:
            func_to_annotations[func] = []
        func_to_annotations[func].append(cls)


    def __call__(self, *args, **kwargs):
        return self.__func(*args, **kwargs)


    @classmethod
    def get_annotated(cls):
        """
        List of functions with this annotat    
        """

        if cls in annotations_to_funcs:
            return annotations_to_funcs[cls]
        return []