# Finance manager

This is a simple finance manager cli application built using Python.

## Features
- Add income and expenses
- View balance
- View transaction history
- Export data to JSON file
- Import data from JSON file

## Installation (create venv and run the script)
1. Clone the repository
2. Navigate to the project directory
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Run the script:
6. ```bash
   python finance_manager.py
   ```
   
-------
### test multiline commite 1
```bash
git commit -m "Заголовок\n\nПодробное описание на новой строке"
```

### test multiline commite 2
```bash
git commit -m "feat: Добавить механизм авторизации" \
-m "- Добавлена библиотека JWT
- Реализована проверка токена
- Закрыт доступ к методам API

Это решает проблему несанкционированного доступа к данным пользователей."
```

Doesn't work in Windows cmd, but works in Git Bash and PowerShell. In Windows cmd, you can use the following command to achieve the same result:

```bash
git commit -m "Заголовок" -m "Подробное описание на новой строке"
```