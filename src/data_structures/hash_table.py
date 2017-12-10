"""Implements a hash table."""


def additive_hash(value):
    """Get the hash value by adding up the value of the chars in a string."""
    if not isinstance(value, str):
        raise TypeError('Value must be a string.')
    return sum(ord(ch) for ch in value)


def fnv_hash(value, offset=2166136261, prime=16777619):
    """Get the hash value using the Fowler-Noll-Vo method.

    Default is the 32-bit version. The initial hash value is the
    FNV offset basis. For each byte in the input, the hash is
    multiplied by the FNV prime, then XOR with the byte from the input.
    """
    if not isinstance(value, str):
        raise TypeError('Value must be a string.')

    hash_val = offset
    for ch in value:
        hash_val = (hash_val * prime) ^ ord(ch)

    return hash_val


class HashTable(object):
    """Structure for items in a hash table.

    A hash table stored values under keys. It hashes the key using
    the hashing function to get a number and stores the value under
    that number, making for easy retrieval.
    """

    def __init__(self, size, hashing):
        """Create an empty hash table.

        size: int, the number of slots to store data in the table
        hashing: funct, the hashing function used for hashing keys
        """
        self.values = [[] for _ in range(size)]
        self.hashing = hashing

    def _hash(self, key):
        """Get the hash value for a string using the hashing function."""
        return self.hashing(key)

    def set(self, key, value):
        """Set the value to the key in the hash table.

        Adds the key if it is not in the table. Replaces the value if
        it is already in the table.
        """
        try:
            slot = self._hash(key) % len(self.values)
        except TypeError:
            raise TypeError('Key must be a string.')

        if self.values[slot]:
            for bucket in self.values[slot]:
                if bucket[0] == key:
                    bucket[1] = value
                    return

        self.values[slot].append([key, value])

    def get(self, key):
        """Get the value stored with the given key."""
        try:
            slot = self._hash(key) % len(self.values)
        except TypeError:
            raise TypeError('Key must be a string.')

        for bucket in self.values[slot]:
            if bucket[0] == key:
                return bucket[1]

        raise KeyError('Key is not in the hash table.')
