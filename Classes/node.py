class Node:
    def __init__(self, name, id=-1):
        self.m_id = id
        self.m_name = name

    def __str__(self):
        return self.m_name

    def change_id(self, id):
        self.m_id = id
