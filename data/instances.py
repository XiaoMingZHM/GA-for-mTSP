
'''
https://github.com/picashuo/opgamoea.git
'''

instance_list =[
    "mtsp51.txt",
    "mtsp100.txt",
    "mtsp150.txt",
    "pr76.txt",
    "pr152.txt",
    "pr226.txt",
]

class instance:
    def __init__(self, file_name):
        with open(file_name, mode='r') as file:
            line = file.readline()
            line = line.splitlines()[0]
            self.size = int(line)
            self.values = []
            while True:
                line = file.readline()
                if not line:
                    break
                line = line.splitlines()[0]
                blocks = line.split(" ")
                value = []
                for ele in blocks:
                    value.append(int(ele))
                self.values.append(value)

    def __str__(self):
        info = f"Size:[{self.size}]; Data: {self.values};"
        return info

if __name__ == '__main__':
    data = instance("mtsp51.txt")
    print(data)