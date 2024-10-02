import math

# Öklid mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# 2D uzaydaki noktaları temsil eden liste (tuple listesi)
points = [(1, 2), (4, 6), (5, 3), (7, 8), (2, 9)]

# Mesafeleri tutacak liste
distances = []

# Mesafelerin hesaplanması
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

# Sonuçların yazdırılması
print("Noktalar arasındaki mesafeler:", distances)
print("Minimum mesafe:", min_distance)
