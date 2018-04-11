import unittest
from undname import undname, UndnameFailure, UNDNAME_COMPLETE


class UndnameTests(unittest.TestCase):

    def test_empty(self):
        res = undname("")

        self.assertEqual("", res)

    def test_unmangled(self):
        res = undname("main")

        self.assertEqual("main", res)

    def test_mangled_complete(self):
        res = undname("?xyz@?$abc@V?$def@H@@PAX@@YAXXZ", UNDNAME_COMPLETE)

        self.assertEqual(
            "void __cdecl abc<class def<int>,void *>::xyz(void)", res)

    def test_mangled_name_only(self):
        res = undname("?xyz@?$abc@V?$def@H@@PAX@@YAXXZ")

        self.assertEqual(
            "abc<def<int>,void *>::xyz", res)

    def test_raises_on_error(self):
        with self.assertRaises(UndnameFailure):
            undname("?")
