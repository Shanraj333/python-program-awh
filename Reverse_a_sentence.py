def reverse(sentence):
    rev=" ".join(word[::-1] for word in sentence.split())
    return rev
input_string=input("Enter a string:")
output_string=reverse(input_string)
print(output_string)
