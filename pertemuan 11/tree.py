import time  # Modul untuk mengukur waktu

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Fungsi untuk menyisipkan elemen ke dalam tree
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# Fungsi inorder traversal untuk mendapatkan elemen dalam urutan yang terurut
def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.value)
        inorder_traversal(root.right, result)

# Fungsi utama untuk Tree Sort
def tree_sort(arr):
    if not arr:  # Jika array kosong, kembalikan array kosong
        return []
    root = None
    for value in arr:
        root = insert(root, value)
    sorted_arr = []
    inorder_traversal(root, sorted_arr)
    return sorted_arr

# Contoh penggunaan
if __name__ == "__main__":
    data = [7, 3, 9, 1, 5, 8, 2]
    print("Data sebelum diurutkan:", data)
    
    # Mulai pengukuran waktu
    start_time = time.time()
    
    sorted_data = tree_sort(data)
    
    # Akhiri pengukuran waktu
    end_time = time.time()
    
    print("Data setelah diurutkan:", sorted_data)
    print(f"Lama waktu pengurutan: {end_time - start_time:.6f} detik")
