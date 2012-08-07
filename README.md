PyAnnotations
=============
Create decorator inherited from `Annotation` class then you can get list of functions which was annotated
with this decorator (`Annotation.get_annotated()` method).
Also you can get list of decorators (inherited from `Annotation`) used for specified function
(`get_annotaions(func)` method)

Usage
-----

    from PyAnnotations import Annotation, get_annotaions

    class Positive(Annotation):
        pass

    @Positive
    def g(t):
        pass

    @Positive
    def test(x):
    print x



    print Positive.get_annotated()
[ &lt; function g at 0x9dc3aac &gt; , &lt; function test at 0x9dcc87c &gt; ]

    get_annotaions(g)
[__main__.Positive]

Note
----
This is one of the first things I wrote in Python. You are wellcome with any suggestion, comments and bugreports.
Also it's my first project on GitHUb