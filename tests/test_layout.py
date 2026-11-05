"""Структура проекта: код лежит в пакете animax/, а программа видит все свои файлы.

Сервер молча работает без онлайн-источников, если их модуль не импортировался. Поэтому ошибка в импортах
не уронила бы программу, а незаметно убрала бы озвучки — здесь это проверяется отдельно.
"""
import os
import sys
import tempfile
import unittest
import uuid
from pathlib import Path

os.environ["APPDATA"] = os.path.join(tempfile.gettempdir(), f"animax-test-{uuid.uuid4().hex[:8]}")
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


class LayoutTest(unittest.TestCase):
    def test_online_sources_are_available(self):
        from animax import server
        self.assertIsNotNone(server.online)

    def test_app_files_live_in_package(self):
        from animax import config
        self.assertEqual(config.APP_DIR, ROOT / "animax")
        for name in ("web/index.html", "animax.ico", "notify_toast.ps1"):
            self.assertTrue((config.APP_DIR / name).is_file(), name)

    def test_no_modules_in_root(self):
        self.assertEqual([p.name for p in ROOT.glob("*.py")], [])


if __name__ == "__main__":
    unittest.main()
