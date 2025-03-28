# Description:
# Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.

# Examples
# "Hi!"     ---> "Hi"
# "Hi!!!"   ---> "Hi!!"
# "!Hi"     ---> "!Hi"
# "!Hi!"    ---> "!Hi"
# "Hi! Hi!" ---> "Hi! Hi"
# "Hi"      ---> "Hi"


def remove(s):
    output = ""
    if (s!=""):
        if (s[len(s)-1] == "!"):
            for x in range(0,len(s)-1):
                output += s[x]
        else:
            output = s
    else:
        output = s
    return output