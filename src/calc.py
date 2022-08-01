class Caluculator():
    def sum(self, left, right):
        if left < 0 or right < 0:
            raise ValueError("left or right is minus value")
        return left + right
    
    def sub(self, left, right):
        return left - right

    def save(self, value):
        repository = FileRepository()
        repository.save("result.txt", value)


class FileRepository(object):
    def save(self, file_path, data):
        raise ValueError("Not implemented")