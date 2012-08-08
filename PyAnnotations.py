def get_undecorated(func):

    while hasattr(func, "_Annotation__func"):
        func = func._Annotation__func
    return func

def get_annotations(func):
    """
    Get list of annotations for current object
    """
    #There func must be actually annotation object
    if not isinstance(func, Annotation):
        return []

    #Check is it annotation
    if hasattr(func, "_Annotation__func"):
        func_key = get_undecorated(func)
        if  func_key in Annotation.func_to_annotations:
            return Annotation.func_to_annotations[func_key]

    return  []


class Annotation(object):
    """
    Base class for annotations
    """

    annotations_to_funcs = {}
    func_to_annotations = {}

    def __init__(self, func, *args, **kwargs):
        self.__func = func
        cls = self.__class__

        func_key = get_undecorated(func)

        if not cls in Annotation.annotations_to_funcs:
            Annotation.annotations_to_funcs[cls] = []
        Annotation.annotations_to_funcs[cls].append(func_key)

        if not func_key in Annotation.func_to_annotations:
            Annotation.func_to_annotations[func_key] = []
        Annotation.func_to_annotations[func_key].append(cls)


    def __call__(self, *args, **kwargs):
        return self.__func(*args, **kwargs)


    @classmethod
    def get_annotated(cls):
        """
        List of functions with this annotat
        """

        if cls in Annotation.annotations_to_funcs:
            return Annotation.annotations_to_funcs[cls]
        return []

