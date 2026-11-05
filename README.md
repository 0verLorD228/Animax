<p align="center">
  <img src="animax/web/icon-128.png" width="96" height="96" alt="Логотип Animax">
</p>

<h1 align="center">Animax</h1>

<p align="center">Аниме-клиент для Windows: каталог, онлайн-озвучки, закладки и свой плеер в одном окне.</p>

<p align="center">
  <a href="https://github.com/0verLorD228/Animax/releases/latest"><img src="https://img.shields.io/github/v/release/0verLorD228/Animax?label=%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F" alt="Последняя версия"></a>
  <a href="https://github.com/0verLorD228/Animax/releases"><img src="https://img.shields.io/github/downloads/0verLorD228/Animax/total?label=%D1%81%D0%BA%D0%B0%D1%87%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" alt="Скачивания"></a>
  <a href="https://github.com/0verLorD228/Animax/actions/workflows/build.yml"><img src="https://github.com/0verLorD228/Animax/actions/workflows/build.yml/badge.svg" alt="Сборка"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/0verLorD228/Animax?label=%D0%BB%D0%B8%D1%86%D0%B5%D0%BD%D0%B7%D0%B8%D1%8F" alt="Лицензия MIT"></a>
</p>

<p align="center">
  <a href="https://github.com/0verLorD228/Animax/releases/latest"><b>Скачать</b></a> ·
  <a href="#возможности">Возможности</a> ·
  <a href="#вопросы-и-проблемы">Вопросы и проблемы</a> ·
  <a href="#дисклеймер">Дисклеймер</a>
</p>

<p align="center">
  <img src=".github/assets/home.png" alt="Главный экран Animax">
</p>

## Возможности

- Каталог Shikimori: поиск, фильтры, расписание, рекомендации, коллекции.
- Онлайн-озвучки Anixart, AniLiberty и Kodik с выбором серии и качества.
- Свой плеер: качества, субтитры, скорость, автопереход и горячие клавиши.
- Списки «Смотрю», «В планах», «Просмотрено», «Отложено», «Брошено», а также оценки, заметки и история.
- Уведомления о новых сериях, премьерах и ответах — в приложении и в Windows.
- Медиатека: свои папки с видео и субтитрами.
- Синхронизация закладок и оценок с Shikimori, если войти в аккаунт.
- Значок в трее, отдельное окно плеера и режим «поверх всех окон».
- Лёгкий режим для слабых компьютеров включается сам.

<table>
  <tr>
    <td><img src=".github/assets/catalog.png" alt="Каталог"></td>
    <td><img src=".github/assets/title.png" alt="Страница тайтла"></td>
  </tr>
</table>

## Скачать и установить

Все файлы — на [странице последнего релиза](https://github.com/0verLorD228/Animax/releases/latest).

| Файл | Что это |
|---|---|
| `Animax-1.0.0-win64-setup.exe` | Установщик. Права администратора не нужны, Animax появится в меню «Пуск». |
| `Animax.exe` | Портативная версия: запускается без установки. |

**Что нужно:** Windows 10 или 11 (64 бита), Microsoft Edge (в этих системах он уже есть) и интернет для каталога и онлайн-озвучек. Комфортно работает на 4 ГБ памяти и 2 ядрах.

Обновляется Animax вручную: скачай новую версию со страницы релизов. Закладки и настройки хранятся отдельно, в `%APPDATA%\Animax`, и при обновлении или удалении программы остаются на месте.

## Вход в Shikimori

Смотреть каталог и озвучки можно без аккаунта. Вход нужен для синхронизации закладок и оценок, комментариев и отзывов.

Для входа нужно один раз создать своё приложение на Shikimori и вставить два ключа. Пошаговая инструкция есть в программе: **Настройки → Аккаунт**. Ключи и данные входа хранятся только на твоём компьютере.

## Вопросы и проблемы

<details>
<summary><b>Windows пишет «Windows защитила ваш компьютер»</b></summary>

Это предупреждение SmartScreen: у программы нет платной цифровой подписи. Нажми «Подробнее» → «Выполнить в любом случае».
</details>

<details>
<summary><b>Антивирус удаляет Animax.exe</b></summary>

Однофайловые сборки PyInstaller иногда ошибочно определяются как угроза, например `Trojan:Win32/Bearfoos.B!ml`. Скачивай Animax только со страницы релизов этого репозитория. Если не хочешь использовать exe, [запусти программу из исходников](.github/CONTRIBUTING.md#запуск-из-исходников).
</details>

<details>
<summary><b>Пишет, что порт 8790 занят</b></summary>

Этот порт заняла другая программа. Закрой её или перезагрузи компьютер, затем запусти Animax снова.
</details>

<details>
<summary><b>Крестик закрыл окно, но Animax работает</b></summary>

Так задумано: программа остаётся в трее. Чтобы закрыть её полностью, нажми «Выход» в приложении или в меню значка у часов.
</details>

Не нашёл ответа — [создай Issue](https://github.com/0verLorD228/Animax/issues).

## Для разработчиков

Запуск из исходников, тесты, структура проекта и сборка описаны в [CONTRIBUTING](.github/CONTRIBUTING.md). Как сообщить об уязвимости — в [SECURITY](.github/SECURITY.md). История версий — в [CHANGELOG](CHANGELOG.md).

## Дисклеймер

> [!IMPORTANT]
> Animax — неофициальный клиент для личного использования. Он не хранит и не размещает видео: программа показывает материалы сторонних сервисов. Проект не связан с Shikimori, Anixart, AniLiberty, Kodik и правообладателями. Все права на видео, обложки, описания и другие материалы принадлежат их владельцам.

Лицензия [MIT](LICENSE) относится только к коду Animax и не даёт прав на контент третьих лиц. Если ты правообладатель и хочешь сообщить о проблеме, [создай Issue](https://github.com/0verLorD228/Animax/issues).

Плеер использует библиотеку [hls.js](https://github.com/video-dev/hls.js) ([Apache-2.0](animax/web/vendor/hls.js.LICENSE.txt)).
