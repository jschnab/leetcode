class DNode:
    def __init__(self, val=0, next_=None, prev=None):
        self.val = val
        self.next = next_
        self.prev = prev


class DList:
    def __init__(self, items=None):
        self.length = 0
        self.first = self.last = None
        if items:
            for i in items:
                self.append(i)

    def append(self, value):
        self.length += 1
        if not self.last:
            self.last = DNode(value)
            self.first = self.last
        else:
            self.last.next = DNode(value, prev=self.last)
            self.last = self.last.next

    def pop(self):
        if self.first:
            self.length -= 1
            value = self.first.val
            if self.first == self.last:
                self.first = self.last = None
            else:
                self.first = self.first.next
                self.first.prev = None
            return value

    @property
    def is_empty(self):
        return self.length == 0

    def __len__(self):
        return self.length
