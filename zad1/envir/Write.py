def generate_output(filename, objects):
    """
    Write output
    - w pierwszej linii liczba wszystkich wczytanych obiektów
    - w drugiej linii ilość obiektów zawierających błędy
    - w trzeciej linii wszystkie obiekty które nie zawierały błędów, zapisane w formie i kolejności, w jakiej wystąpiły w pliku "input.txt"
    """
    with open(filename, "w") as file:
        # Writing data to a file
        number_of_all_objects = bin(len(objects))[2:]

        # liczba wszystkich wczytanych obiektów
        file.writelines(number_of_all_objects)
        file.writelines("\n")

        # ilość obiektów zawierających błędy
        number_of_bugs = bin(number_of_objects_bugs(objects))[2:]
        file.writelines(number_of_bugs)
        file.writelines("\n")

        # obiekty które nie zawierały błędów
        new_list_object = object_without_error(objects)
        for obj in new_list_object:
            file.writelines(obj.object_write)


def number_of_objects_bugs(objects):
    number_of_bugs = 0
    for obj in objects:
        if obj.check_error():
            number_of_bugs += 1
    return number_of_bugs

def object_without_error(objects):
    new_list_object = []
    for obj in objects:
        if not obj.check_error():
            new_list_object.append(obj)

    return new_list_object