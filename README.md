<img width="1171" height="694" alt="demo (2)" src="https://github.com/user-attachments/assets/fc3493e6-9ab7-450a-a15d-cb6bbac171c8" /># 1. Аналитика каталога стримингового сервиса.

Проект содержит 9 этапов.

## 2. Инструменты:
- **Python** 3.12
- **uv** — управление проектом
- **Ruff** — линтер для проверки стиля кода

## 3. Структура проекта:
- `catalog_analysis.py` — исполняемый файл
- `pyproject.toml`, `uv.lock`, `.gitignore` — конфигурация проекта, версии зависимостей

## 4. Запуск проекта:
Запускается командой

Запуск итогового отчета по каталогу выполняется командой:
```
uv run catalog_analysis.py
```

Линтер Ruff
Проверка стиля кода и форматирования запускается командой:

```
uv run ruff check .
```

## 5. Демонстрация в asciinema

<img width="1171" height="694" alt="demo (2)" src="https://github.com/user-attachments/assets/959c94ce-4215-478f-9fa6-584b5024cae4" />
