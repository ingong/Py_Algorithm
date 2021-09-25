## Py_Algorithm

1일 1알고리즘 실천을 위한 레포지토리입니다.

<br/>

## 자료구조

### 1. Binary Heap

```python
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
      self.items[idx], self.items[smallest] = \
        self.items[smallest], self.items[idx]
      self._prelocate_down(smallest)

  def extract(self):
    extracted = self.items[1]
    self.items[1] = self.items[len(self)]
    self.items.pop()
    self._prelocate_down(1)
    return extracted
```

- **len 메서드**

  - 마지막 요소를 가져오기 위한 함수
  - 기존의 len 함수와는 다르다, 트리구조는 1부터 index 가 시작

- **insert, prelocate_up 메서드 : 요소를 Heap 에 삽입**

  - 가장 하위 레벨의 최대한 왼쪽으로 삽입 (배열의 경우 맨 마지막에 삽입)
  - 부모값과 비교해 값이 더 작은 경우 위치를 변경
  - 계속해서 부모 값과 비교해 위치를 변경 (가장 작은 값일 경우 루트까지 올라감)

- **extract, prelocate_down 메서드 : 최상위 요소를 Heap 에서 추출 후, 힙 자료구조 유지위한 작업**
  - 최상위 값을 제거하고, heap 특성 유지하는 작업이 필요하기 때문에 시간 복잡도는 O(logn)

<br/>

### Reference

- 파이썬 알고리즘 인터뷰
