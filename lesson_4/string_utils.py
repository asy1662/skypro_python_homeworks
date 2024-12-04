class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """

    def capitalize(self, string: str) -> str:
        """
        Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст.
        Пример: `capitalize("skypro") -> "Skypro"`
        """
        return string.capitalize()

    def trim(self, string: str) -> str:
        """
        Принимает на вход текст и удаляет пробелы в начале, если они есть.
        Пример: `trim(" skypro") -> "skypro"`
        """
        return string.lstrip()

    def to_list(self, string: str, delimiter: str = ",") -> list[str]:
        """
        Принимает на вход текст с разделителем и возвращает список строк.

        Параметры:
        `string` - строка для обработки
        `delimiter` - разделитель строк. по умолчанию запятая (",")

        Пример 1: `to_list("a,b,c,d") -> ["a", "b", "c", "d"]`
        Пример 2: `to_list("1:2:3", ":") -> ["1", "2", "3"]`
        """
        if self.is_empty(string):
            return []

        return string.split(delimiter)

    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает `true`, если строка содержит искомый символ и `false` - если нет

        Параметры:
        `string` - строка для обработки
        `symbol` - искомый символ

        Пример 1: `contains("skypro", "s") -> true`
        Пример 2: `contains("skypro", "u") -> false`
        """
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки

        Параметры:
        `string` - строка для обработки
        `symbol` - искомый символ для удаления

        Пример 1: `delete_symbol("skypro", "k") -> "sypro"`
        Пример 2: `delete_symbol("skypro", "pro") -> "sky"`
        """
        return string.replace(symbol, "")

    def starts_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает `true`, если строка начинается с заданного символа и `false` - если нет

        Параметры:
        `string` - строка для обработки
        `symbol` - искомый символ

        Пример 1: 'starts_with("skypro", "s") -> true`
        Пример 2: 'starts_with("skypro", "p") -> false`
        """
        return string.startswith(symbol)

    def ends_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает `true`, если строка заканчивается заданным символом и `false` - если нет

        Параметры:
        `string` - строка для обработки
        `symbol` - искомый символ

        Пример 1: `ends_with("skypro", "o") -> true`
        Пример 2: `ends_with("skypro", "y") -> false`
        """
        return string.endswith(symbol)

    def is_empty(self, string: str) -> bool:
        """
        Возвращает `true`, если строка пустая и `false` - если нет

        Пример 1: `is_empty("") -> true`
        Пример 2: `is_empty(" ") -> true`
        Пример 3: `is_empty("skypro") -> false`
        """
        return len(string.strip()) == 0

    def list_to_string(self, lst: list, joiner: str = ", ") -> str:
        """
        Преобразует список элементов в строку с указанным разделителем

        Параметры:
        `lst` - список элементов
        `joiner` - разделитель элементов в строке. по умолчанию запятая (", ")

        Пример 1: `list_to_string([1,2,3,4]) -> "1, 2, 3, 4"`
        Пример 2: `list_to_string(["sky", "pro"]) -> "sky, pro"`
        Пример 3: `list_to_string(["sky", "pro"], "-") -> "sky-pro"`
        """
        return joiner.join(map(str, lst))
