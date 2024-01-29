def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)

    else:
        print("Recursion Example Results")
        return 0
    return result
tri_recursion(7)