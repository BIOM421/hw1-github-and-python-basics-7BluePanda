
def hello_world():
    # print("Hello World!")
    return "Hello World!"

def hello_world_n(N):
    hellostring = ""
    for ii in range(N):
        hellostring = hellostring + hello_world() + " "
        
    return hellostring

