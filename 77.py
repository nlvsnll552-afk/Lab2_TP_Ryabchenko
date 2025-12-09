import urllib.request

class MyFileURL:
    def __init__(self, target, mode):
        self.target = target
        self.mode = mode
    
    def read(self):
        if self.mode == "url": # открывает URL и читает содержимое как текст (декодирует из бит в строку)
            return urllib.request.urlopen(self.target).read().decode('utf-8')
        if self.mode != "read" and self.mode != "url": # если режим не "read" и не "url" выбрасывает ошибку
            raise ValueError("Для чтения используйте режим 'read' или 'url'")
        if self.mode == "read":
            with open(self.target, 'r', encoding='utf-8') as f: # открывает файл
                return f.read()
    
    def write(self, content):
        if self.mode not in ["write", "append"]: # Проверка на ошибку
            raise ValueError("Для записи используйте режим 'write' или 'append'")
        mode_flag = 'w' if self.mode == "write" else 'a' # определение флага перезаписи или добавления
        with open(self.target, mode_flag, encoding='utf-8') as f: # открывает файл с нужным флагом и записыает строку
            f.write(content)
    
    def read_url(self):
        if self.mode != "url": # Проверка на ошибку 
            raise ValueError("Только в режиме 'url'")
        return urllib.request.urlopen(self.target).read().decode('utf-8') # открывает URL и читает содержимое как текст
    
    def write_url(self, filename):
        if self.mode != "url": # Проверка на ошибку
            raise ValueError("Только в режиме 'url'")
        with open(filename, 'w', encoding='utf-8') as f: # читает содержимое URL через read_url() и записывает в указанный файл
            f.write(self.read_url())
