from fabric.colors import blue, cyan, green, magenta, red, white, yellow

def print_info(message="This is a customer service announcement."):
    print(green(message))

def print_warning(message="There is no access to the root account until further notice."):
    print(yellow(message))

def print_error(message="Leaves on tracks. All services are cancelled."):
    print(red(message))

print_info()
print_warning()
print_error()
