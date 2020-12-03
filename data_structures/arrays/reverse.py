
def reverse(string_item):

    #check for instance type 

    if isinstance(string_item, str) and len(string_item) < 2:

        return "Input is not a string"

    backward_input = []

    for i in range(len(string_item)-1, -1, -1):
        backward_input.append(string_item[i])
    

    backward_input = "".join(backward_input)
   

    return backward_input

    #return string_item[::-1]


if __name__ == "__main__":

  print(reverse("I went to Stuttgart"))