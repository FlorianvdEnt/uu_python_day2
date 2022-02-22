
class Fish:
    def __init__(self):
        self.members = ['Harring', 'Salmon']

    def print_members(self):
        print('Members of mammels class:')
        for member in self.members:
            print(f'\t{member}')

