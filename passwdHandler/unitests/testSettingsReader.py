from unittest import TestCase, main
from .passwdHandler.core.components.settingsReader import SettingsReader
# import ..core/components/settingsReader.PasswdSettings


class TestSettingsReader(TestCase):
    def setUp(self) -> None:
        self.settingsReaderInstance = PasswdSettings()
        return super().setUp()
    
    def test_search_setting(self) -> None:
        self.assertEqual(self.settingsReaderInstance.read_setting('lowercase'), True)


if __name__ == '__main__':
    main()