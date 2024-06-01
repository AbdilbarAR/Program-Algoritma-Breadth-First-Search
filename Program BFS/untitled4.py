from collections import defaultdict, deque

# Fungsi untuk menjalankan algoritma BFS
def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_node, path = queue.popleft()
        visited.add(current_node)

        if current_node == goal:
            return path

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return None  # Jika tidak ada rute yang ditemukan

while True:
    # Meminta input dari pengguna untuk mencari rute terdekat
    graph = defaultdict(list)
    n = int(input("Masukkan jumlah simpul (nodes) dalam grafik: "))

    for i in range(n):
        node = input(f"Masukkan nama simpul (node) ke-{i+1}: ")
        neighbors = input(f"Masukkan tetangga dari {node} (pisahkan dengan spasi): ").split()
        graph[node] = neighbors

    start_node = input("Masukkan simpul awal: ")
    goal_node = input("Masukkan simpul tujuan: ")

    # Menemukan rute terdekat
    result = bfs(graph, start_node, goal_node)

    if result:
        print(f"Rute terdekat dari {start_node} ke {goal_node} adalah: {' -> '.join(result)}")
    else:
        print("Tidak ada rute yang ditemukan.")

    # Meminta input untuk mencoba lagi atau keluar
    try_again = input("Coba lagi? (ya/tidak): ")
    if try_again.lower() != 'ya':
        break