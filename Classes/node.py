class Node:
    def __init__(self, name, id=-1):
        self.m_id = id
        self.m_name = str(name)

    def __str__(self):
        return self.m_name
        
    def __repr__(self):
        return self.m_name


    def change_id(self, id):
        self.m_id = id

    def __eq__(self, other):
        return self.m_name == other.m_name

    def __hash__(self):
        return hash(self.m_name)