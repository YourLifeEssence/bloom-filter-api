import hashlib

class BloomFilter:
    def __init__(self, size, hash_funcs):
        self.size = size
        self.hash_funcs = hash_funcs
        self.bit_array = [0] * size

    def _get_indices(self, key):
        return [hf(str(key).encode()) % self.size for hf in self.hash_funcs]

    def insert(self, key):
        for idx in self._get_indices(key):
            self.bit_array[idx] = 1

    def contains(self, key):
        return all(self.bit_array[idx] for idx in self._get_indices(key))

def hash_md5(data): return int(hashlib.md5(data).hexdigest(), 16)
def hash_sha1(data): return int(hashlib.sha1(data).hexdigest(), 16)
def hash_sha256(data): return int(hashlib.sha256(data).hexdigest(), 16)