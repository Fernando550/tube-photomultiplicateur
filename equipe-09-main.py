import matplotlib.pyplot as ptl


squares = [1,2,3,4]

def run():
    fig, ax = ptl.subplots()
    ax.plot(squares)

    ptl.show()

if __name__ == "__main__":
    run()