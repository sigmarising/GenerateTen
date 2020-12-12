def main():
    result = []
    for i1 in range(0,10):
        for i2 in range(0,10):
            for i3 in range(0,10):
                for i4 in range(0,10):
                    if i1 + i2 + i3 + i4 == 10:
                        result.append([i1, i2, i3, i4])
    
    with open("./GetResult.txt", "w") as f:
        f.write(str(result))
    print("See GetResult.txt")

if __name__ == "__main__":
    main()