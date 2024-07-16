import os
from pysmi.reader import FileReader
from pysmi.writer import PyFileWriter
from pysmi.parser import SmiStarParser
from pysmi.codegen import YamlGenerator

# Указать путь к директории с MIB-файлами и YAML-файлами
mib_folder = r'C:\Users\mramishvili\Downloads\YEASTAR-P-SERIES-V1.mib'


yaml_folder = r'C:\Users\mramishvili\Downloads\YEASTAR-P-SERIES-V1.yaml'

# Получить список MIB-файлов в директории
mib_files = os.listdir(mib_folder)

# Создать папку для YAML-файлов, если ее еще нет
if not os.path.exists(yaml_folder):
    os.makedirs(yaml_folder)

# Пройти по каждому MIB-файлу и преобразовать его в YAML
for mib_file in mib_files:
    if mib_file.endswith('.mib'):
        # Открыть MIB-файл
        mib_reader = FileReader(os.path.join(mib_folder, mib_file))

        # Создать YAML-файл
        yaml_file = os.path.join(yaml_folder, mib_file.replace('.mib', '.yaml'))
        yaml_writer = PyFileWriter(yaml_file)

        # Создать парсер MIB-файла
        mib_parser = SmiStarParser()

        # Создать генератор YAML
        yaml_generator = YamlGenerator()

        # Преобразовать MIB-файл в YAML
        mib_module = mib_parser.parse(mib_reader)
        yaml_generator.generate(mib_module, yaml_writer)
