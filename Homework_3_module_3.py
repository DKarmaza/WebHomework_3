import os
import shutil
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def copy_file(file_path, target_directory):
    ext = file_path.suffix[1:]
    target_folder = target_directory / ext
    target_folder.mkdir(parents=True, exist_ok=True)
    shutil.copy(file_path, target_folder / file_path.name)
    print(f"Створення копії з {file_path} до {target_folder}")

def process_directory(source_directory, target_directory):
    with ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(source_directory):
            for file in files:
                file_path = Path(root) / file
                executor.submit(copy_file, file_path, target_directory)

def main():
    # Введення шляхів до директорій від користувача
    source_directory = Path(input("Введіть шлях до директорії, яку треба скопіювати: ").strip())
    target_directory = Path(input("Введіть шлях до директорії, куди копіювати (або залиште порожнім для 'dist'): ").strip() or 'dist')

    # Перевірка чи існує джерельна директорія
    if not source_directory.exists():
        print(f"Джерельна директорія {source_directory} не знайдена!")
        return

    if not target_directory.exists():
        target_directory.mkdir(parents=True)

    process_directory(source_directory, target_directory)

if __name__ == "__main__":
    main()