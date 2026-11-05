# Разработка Animax

Animax — локальный сервер на Python и интерфейс на HTML, CSS и JavaScript, который открывается в окне Microsoft Edge. Работает только на Windows.

## Запуск из исходников

Нужен Python 3.10 или новее. Сервер использует только стандартную библиотеку; [Pillow](https://pypi.org/project/pillow/) необязателен и нужен для обработки обложек.

```bat
git clone https://github.com/0verLorD228/Animax.git
cd Animax
python Animax.pyw
```

Чтобы проверять правки, не трогая свои закладки, запусти только сервер с временной папкой данных и открой адрес из консоли в браузере:

```powershell
$env:APPDATA = "$env:TEMP\animax-test"
python -m animax.server 8799
```

## Структура

```text
Animax.pyw        запуск: один экземпляр, окно, трей, протокол animax:
animax/
  server.py       локальный HTTP-сервер, API, защита Host и Origin
  config.py       пути и общие настройки
  state.py        закладки и настройки, слияние изменений из разных окон
  shiki_*.py      Shikimori: сеть, данные, вход, коллекции
  reviews.py      отзывы Shikimori
  sources.py      онлайн-озвучки: Anixart, AniLiberty, Kodik
  media.py        медиатека, субтитры, обложки
  windows.py      окна Edge и уведомления Windows
  tray.py         значок в трее
  sysinfo.py      определение слабого компьютера
  web/            интерфейс и hls.js
packaging/        сборка exe и установщика
tests/            автотесты
```

Данные программы лежат в `%APPDATA%\Animax`. Токены и ключи хранятся только там и не попадают в репозиторий.

## Тесты

Юнит-тесты не требуют интернета и не трогают настоящие данные:

```bat
python -m unittest discover -s tests
```

Если меняются сеть или интерфейс, запусти ещё проверку в настоящем браузере. Ей нужны Edge, интернет и `pip install playwright`:

```bat
python tests\ui_smoke.py
```

## Правила кода

- Стиль — как в окружающем коде: короткие функции, а комментарии на русском объясняют «почему», а не «что».
- Для нового поведения и исправленной ошибки сначала пишется тест, который падает, потом код.
- Токены, ключи и другие секреты в репозиторий не попадают.
- Новые зависимости добавляются только при реальной необходимости.

## Сборка

```bat
python -m pip install -r packaging\requirements-build.txt
python packaging\build.py
```

Готовый файл: `..\Сборка Animax\Animax.exe` (один файл, без установки).

Для установщика нужен [Inno Setup 6](https://jrsoftware.org/isinfo.php):

```bat
winget install JRSoftware.InnoSetup
python packaging\build_installer.py
```

Результат: `dist\Animax-1.0.0-win64-setup.exe`. Установщик ставит программу в `%LOCALAPPDATA%\Programs\Animax` без прав администратора и кладёт рядом `packaging\README.txt`. Настройки установщика — в `packaging\installer.iss`.

## Релиз

CI собирает exe и установщик при каждом пуше в `main`, а перед сборкой запускает юнит-тесты. Тег вида `v1.0.0` публикует релиз с этими файлами.

При смене версии обнови `packaging\version_info.txt`, `packaging\installer.iss`, `packaging\README.txt`, `APP_VERSION` в `animax\web\js\core.js` и `CHANGELOG.md`.

## Подпись

Exe не подписан, поэтому Windows может показать предупреждение SmartScreen. Чтобы его убрать, нужен сертификат подписи кода и команда вроде:

```powershell
signtool sign /fd SHA256 /tr http://timestamp.digicert.com /td SHA256 /a Animax.exe
```
