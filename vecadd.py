
from concurrent.futures import ThreadPoolExecutor

v1 = list(map(int, input("Enter elements of first vector separated by space: ").split()))
v2 = list(map(int, input("Enter elements of second vector separated by space: ").split()))
def dot_product_parallel(a, b):
    with ThreadPoolExecutor() as executor:
        # Each thread multiplies one pair (x, y)
        results = list(executor.map(lambda x_y: x_y[0] * x_y[1], zip(a, b)))
    return sum(results)

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [5, 4, 3, 2, 1]
    print("Parallel Dot product:", dot_product_parallel(a, b))
    print("hello")
