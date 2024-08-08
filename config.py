"""
Модуль для конфигураций
"""
import os

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

HOST = "localhost"
PORT = 8080


def static_files_path(name: str):
    return os.path.join(ROOT_PATH, 'templates', name)
