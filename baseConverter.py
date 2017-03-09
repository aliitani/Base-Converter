class BaseConverter:

    def __init__(self):
        pass

    def conversion(base, convert_to):
        str_result = ""

        if convert_to > 16:
            str_result = "Converts bases that are less than or equal to 16"
        else:
            alpha = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
            while base >= 1:
                if base % convert_to >= 10:
                    str_result += alpha[base % convert_to]
                    base /= convert_to
                else:
                    str_result += str(base % convert_to)
                    base /= convert_to
            return str_result[::-1]

        return str_result

    conversion = staticmethod(conversion)
