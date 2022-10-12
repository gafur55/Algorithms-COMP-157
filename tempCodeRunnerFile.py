reasing_order:
        start = time.time()
        insertion(i)
        end = time.time()
        decreasing_order_data.append((end - start) * 10**3)
        print("timing for insertion sort with ", len(i), " sized (decreasing ordered) array ---->", (end - start) * 10**3, "ms")
    print()