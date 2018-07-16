def bottles(num_bottles):
    """Takes the starting number to output the '99 bottles of beer on the wall song' that decrements from the
    given value until the singular bottle in the final line at will end the output."""
    first_line = "{0} bottles of beer on the wall. {0} bottles of beer. "
    second_line = "Take one down. Pass it around. {0} bottles of beer on the wall. "
    counter = num_bottles
    output_string = ''
    for bots in range(num_bottles, 1, -1):
        output_string = output_string + first_line.format(counter)
        counter -= 1
        output_string = output_string + second_line.format(counter) + "\n"
    output_string = output_string + "1 bottle of beer on the wall. 1 bottle of beer. Take one down. Pass it around. No more bottles of beer on the wall."
    return output_string

if __name__=="__main__":
    print(bottles(99))
