def reverse_string(string_):

    len_string = len(string_)

    if len_string == 1:
        return string_

    print(string_[len_string-1], end = "")
    return reverse_string(string_[0:len_string-1])


if __name__ == "__main__":
    print(reverse_string("John"))