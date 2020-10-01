from typing import List, Dict

class Heap(object):
    """
    Une heap est une structure de données sous forme d'arbre.
    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """

    def __init__(self, value: int):
        pass

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        pass    

    def find_min(self) -> int:
        return self.min_node

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def decrease_key(self, current_value: int, new_value :int) -> None:
        """
        Modify une valeur dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        """
        Fusionne deux arbres
        """
        pass


class FibonacciHeap():
    """
    Une fibonnaci heap est un arbre permettant de stocker et trier des donnés efficacement
    https://en.wikipedia.org/wiki/Fibonacci_heap
    L'implémentation est décrite en anglais : https://en.wikipedia.org/wiki/Fibonacci_heap#Implementation_of_operations
    et en français : https://fr.wikipedia.org/wiki/Tas_de_Fibonacci#Implémentation_des_opérations
    """
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.parent = self.child = self.left = self.right = None

    root_node, min_node = None, None
    total_nodes = 0

    def insert(self, key, value: int) -> None:
        node_to_insert = self.Node(key, value)
        node_to_insert.left = node_to_insert.right = node_to_insert

        if self.root_node is None:
            self.root_node = node_to_insert
        else:
            node_to_insert.right = self.root_node.right
            node_to_insert.left = self.root_node
            self.root_node.right.left = node_to_insert
            self.root_node.right = node_to_insert
        
        if self.min_node is None or node_to_insert.key < self.min_node.key:
            self.min_node = node_to_insert
        self.total_nodes += 1
        return node_to_insert
    
    def find_min(self) -> int:
        return self.min_node

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        minimun = self.min_node
        if minimun is not None:
            if minimun == minimun.right:
                self.min_node = self.root_node = None
            else:
                self.min_node = minimun.right
            self.total_nodes -= 1
        return minimun


    def merge(self, fibonnaci_heap: Heap) -> None:
        """
        Fusionne deux arbres
        """
        H = FibonacciHeap()
        H.root_node, H.min_node = self.root_node, self.min_node
        last = fibonnaci_heap.root_node.left
        h2.root_node.left = H.root_node.left
        H.root_node.left.right = fibonnaci_heap.root_node
        H.root_node.left = last
        H.root_node.left.right = H.root_node
        if fibonnaci_heap.min_node.key < H.min_node.key:
            H.min_node = fibonnaci_heap.min_node
        H.total_nodes = self.total_nodes + fibonnaci_heap.total_nodes
        return H


f = FibonacciHeap()

f.insert(0,2)
f.insert(1,4)
f.insert(2,8)
f.insert(3,5)

print(f)

m = f.find_min()
print(m)

q = f.delete_min()
print(q)
