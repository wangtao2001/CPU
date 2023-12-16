# -*- coding : utf-8-*-

class parser():
    file_path: str
    metadata: dict

    def __init__(self, file_path, encoding='utf-8') -> None:
        self.file_path = file_path
        self.metadata = dict()
        file = open(file_path, 'r', encoding=encoding)
        li = [ i.strip() for i in  file.readlines() if i != '\n' and i != '' and not i.startswith('#')]
        config: str = ''
        for i in li:
            if i.startswith('[') and i.endswith(']'):
                self.metadata[i[1:-1]] = {}
                config = i[1:-1]
            else:
                key, value = i.split('=')
                self.metadata[config][key] = value

    def read_dict(self, key) -> dict:
        return self.metadata[key]


    