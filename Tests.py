import unittest
from PyAnnotations import *

class AnnotationRegistration(unittest.TestCase):

    def test_single_annotation(self):
        class AnnotationA(Annotation):
            pass

        @AnnotationA
        def foo():
            pass

        self.assertEqual(get_annotations(foo),[AnnotationA])
        self.assertEqual(AnnotationA.get_annotated(),[get_undecorated(foo)])


    def test_multiple_annotations(self):
        class AnnotationA(Annotation):
            pass

        class AnnotationB(Annotation):
            pass

        class AnnotationC(Annotation):
            pass

        @AnnotationA
        @AnnotationB
        def foo():
            pass

        self.assertItemsEqual(get_annotations(foo),[AnnotationA, AnnotationB])
        self.assertItemsEqual(AnnotationC.get_annotated(),[])

    def test_multiple_funcs(self):
        class AnnotationA(Annotation):
            pass

        @AnnotationA
        def fooA():
            pass

        @AnnotationA
        def fooB():
            pass

        def fooC():
            pass

        self.assertItemsEqual(AnnotationA.get_annotated(),[get_undecorated(fooA), get_undecorated(fooB)])
        self.assertItemsEqual(get_annotations(fooC),[])
        

if __name__ == '__main__':
    unittest.main()
