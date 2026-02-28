import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR_NAME = 'djangotube'
FILENAME = 'manage.py'

# Вариант 1: djangotube/ в корне, manage.py внутри
MANAGE_PATH = os.path.join(BASE_DIR, PROJECT_DIR_NAME)
# Вариант 2: src/ с manage.py и src/djangotube/
if not os.path.isdir(MANAGE_PATH) or not os.path.isfile(os.path.join(MANAGE_PATH, FILENAME)):
    src_path = os.path.join(BASE_DIR, 'src')
    if os.path.isdir(src_path) and os.path.isfile(os.path.join(src_path, FILENAME)):
        MANAGE_PATH = src_path
    elif not os.path.isdir(MANAGE_PATH):
        assert False, (
            f'В директории `{BASE_DIR}` не найдена папка c проектом `{PROJECT_DIR_NAME}` '
            f'(ни `{PROJECT_DIR_NAME}/`, ни `src/` с manage.py). '
            f'Убедитесь, что у вас верная структура проекта.'
        )

if not os.path.isfile(os.path.join(MANAGE_PATH, FILENAME)):
    assert False, (
        f'В директории `{MANAGE_PATH}` не найден файл `{FILENAME}`. '
        f'Убедитесь, что у вас верная структура проекта.'
    )

from django.utils.version import get_version

assert get_version() < '3.0.0', 'Пожалуйста, используйте версию Django < 3.0.0'

from djangotube.settings import INSTALLED_APPS

assert any(app in INSTALLED_APPS for app in ['posts.apps.PostsConfig', 'posts']), (
    'Пожалуйста зарегистрируйте приложение в `settings.INSTALLED_APPS`'
)

pytest_plugins = [
    'tests.fixtures.fixture_user',
    'tests.fixtures.fixture_data',
]
