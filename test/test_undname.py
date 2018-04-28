import unittest
from undname import undname, UndnameFailure


class UndnameTests(unittest.TestCase):

    def test_empty(self):
        res = undname("")

        self.assertEqual("", res)

    def test_unmangled(self):
        res = undname("main")

        self.assertEqual("main", res)

    def test_mangled_complete(self):
        res = undname("?xyz@?$abc@V?$def@H@@PAX@@YAXXZ")

        self.assertEqual(
            "void __cdecl abc<class def<int>,void *>::xyz(void)", res)

    def test_mangled_name_only(self):
        res = undname("?xyz@?$abc@V?$def@H@@PAX@@YAXXZ", name_only=True)

        self.assertEqual(
            "abc<def<int>,void *>::xyz", res)

    def test_raises_on_error(self):
        with self.assertRaises(UndnameFailure):
            undname("?")

    def test_name_only_no_ms_keywords(self):
        res = undname(
            "??B?$PPtr@VLevelGameManager@@@@QEBAPEAVLevelGameManager@@XZ",
            name_only=True, ms_keywords=False)

        self.assertEqual("PPtr<LevelGameManager>::operator LevelGameManager *",
                         res)

    def test_function_in_anonymous_namespace(self):
        res = undname("?ThreadFunc@?A0x6a578590@base@@YAKPEAX@Z", ms_keywords=False)

        self.assertEqual(
            "unsigned long base::`anonymous namespace'::ThreadFunc(void *)",
            res)
