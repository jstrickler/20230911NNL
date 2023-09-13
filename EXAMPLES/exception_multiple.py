import sys

try:
    x = 5
    y = "cheese"
    z = x + y
    f = open("sesame.txt")
    print("Bottom of try")

except (IOError, TypeError) as err:  # Use a tuple of 2 or more exception types
    print("Naughty programmer! ", err)
    sys.exit(1)

finally:
    # remove temp files
    # delete big data structure
    #  etc
    print("DONE")

print("end of script")
