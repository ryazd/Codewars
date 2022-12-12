# https://www.codewars.com/kata/536e7c7fd38523be14000ca2


class MemoryManager:
    def __init__(self, memory):
        """
        @constructor Creates a new memory manager for the provided array.
        @param {memory} An array to use as the backing memory.
        """
        self.memory = memory
        self.alloc = []
        self.size = len(memory)

    def allocate(self, size):
        """
        Allocates a block of memory of requested size.
        @param {number} size - The size of the block to allocate.
        @returns {number} A pointer which is the index of the first location in the allocated block.
        @raises If it is not possible to allocate a block of the requested size.
        """
        alloc = False
        if size > self.size:
            raise MemoryError("Cannot allocate more memory than exists")
        else:
            self.alloc.sort(key=lambda x: x[0])
            if len(self.alloc) == 0 or self.alloc[0][0] >= size:
                alloc = True
                self.alloc.append((0, size))
            else:
                for i in range(len(self.alloc)):
                    if i < len(self.alloc) - 1:
                        if self.alloc[i][1] + size <= self.alloc[i + 1][0]:
                            self.alloc.append((self.alloc[i][1], self.alloc[i][1] + size))
                            alloc = True
                            break
                    elif self.alloc[i][1] + size <= len(self.memory):
                        self.alloc.append((self.alloc[i][1], self.alloc[i][1] + size))
                        alloc = True
                        break
            if alloc:
                self.size -= size
                return self.alloc[-1][0]
            raise MemoryError("Cannot allocate more memory than exists")

    def release(self, pointer):
        """
        Releases a previously allocated block of memory.
        @param {number} pointer - The pointer to the block to release.
        @raises If the pointer does not point to an allocated block.
        """
        i = 0
        length = len(self.alloc)
        while i < length:
            if self.alloc[i][0] == pointer:
                for j in range(pointer, self.alloc[i][1]):
                    self.memory[j] = None
                realised = self.alloc.pop(i)
                self.size += realised[1] - realised[0]
                break
            i += 1
        if i == length:
            return "pointer does not point to an allocated block"

    def read(self, pointer):
        """
        Reads the value at the location identified by pointer
        @param {number} pointer - The location to read.
        @returns {number} The value at that location.
        @raises If pointer is in unallocated memory.
        """
        for i in range(len(self.alloc)):
            if self.alloc[i][0] <= pointer < self.alloc[i][1]:
                return self.memory[pointer]
        raise MemoryError("No memory has been allocated")

    def write(self, pointer, value):
        """
        Writes a value to the location identified by pointer
        @param {number} pointer - The location to write to.
        @param {number} value - The value to write.
        @raises If pointer is in unallocated memory.
        """
        writer = False
        for i in range(len(self.alloc)):
            if self.alloc[i][0] <= pointer < self.alloc[i][1]:
                writer = True
                self.memory[pointer] = value
                break
        if not writer:
            raise MemoryError("No memory has been allocated")


