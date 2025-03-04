from Leaf import File
from Composite import Directory

file1 = File("documento1.txt", 100)
file2 = File("documento2.txt", 200)

sub_directory = Directory("Subdirectorio")
sub_directory.add(file1)

main_directory = Directory("Directorio Principal")
main_directory.add(sub_directory)
main_directory.add(file2)

print(f"Tamaño total: {main_directory.get_size()}")  # 300