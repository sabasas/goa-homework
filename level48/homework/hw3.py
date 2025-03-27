# You need to write a function that reverses the words in a given string. Words are always separated by a single space.

# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

# Example (Input --> Output)

# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"

def reverse(st):
    st2 = ""
    arr = st.split()[::-1]
    for i in arr:
        st2 += i
        if not i == arr[-1]: 
            st2 += ' '
    return st2