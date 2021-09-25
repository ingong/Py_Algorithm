class BinaryHeap(object):
  def __init__(self):
    self.items = [None]
  
  def __len__(self):
    return len(self.items) - 1
  
  def __precolate_up(self):
    i = len(self)
    parent = i // 2
    while parent > 0:
      if self.items[i] < self.items[parent]:
        self.items[i], self.items[parent] = self.items[parent], self.items[i]
      i = parent
      parent = i // 2
  
  def insert(self, k):
    self.items.append(k)
    self.__precolate_up()
  
  def _prelocate_down(self, idx):
    smallest = idx
    left = idx * 2
    right = idx * 2 + 1
    
    if left <= len(self) and self.items[left] < self.items[smallest]:
      smallest = left
    
    if right <= len(self) and self.items[right] < self.items[smallest]:
      smallest = right
      
    if smallest != idx:
      self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
      self._prelocate_down(smallest)
  
  
  def extract(self):
    extracted = self.items[1]
    self.items[1] = self.items[len(self)]
    self.items.pop()
    self._prelocate_down(1)
    return extracted