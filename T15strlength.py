def string_length(s):
    count = 0
    i = 0
    while True:
        try:
            s[i]
            count += 1
            i += 1
        except IndexError:
            break
    return count

# Example usage:
string = "Hello, World!"
print("String:", string)
print("Length:", string_length(string))
