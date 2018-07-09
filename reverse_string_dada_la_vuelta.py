def reverse_string(string_to_reverse):
    string_reversed = ""
    current_index = len(string_to_reverse) -1
    while current_index >= 0:
        string_reversed += string_to_reverse(current_index)
        current_index -= 1
    return string_reversed

print(reverse_string("Hola"))
print(reverse_string("Caracola"))
print(reverse_string("Cacaola"))
print(reverse_string("Me llamo Dave"))
print(reverse_string("Tengo 100 años"))
print(reverse_string("Me duele la cabeza"))