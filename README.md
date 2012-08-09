PyAnnotations
=============
Create decorator inherited from `Annotation` class then you can get list of functions which was annotated
with this decorator (`Annotation.get_annotated()` method).
Also you can get list of decorators (inherited from `Annotation`) used for specified function
(`get_annotaions(func)` method)

License
-------
Copyright (c) 2012 Alexander Borovkov

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
[\_\_main__.Positive]

Notice
------
`get_annotated()` return function __without decorators__. You can undecorate (include only inherited from `Annotaion`
class decorators) by `get_undecorated(func)` method

P.S.
----
This is one of the first things I wrote in Python. You are wellcome with any suggestion, comments and bugreports.
Also it's my first project on GitHUb