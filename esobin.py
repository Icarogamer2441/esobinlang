import sys

def interpret(code):
    lines = code.split("\n")
    bin0 = 0
    bin1 = 0

    for line in lines:
        tokens = list(line)

        if tokens[0] == "3":
            pass
        else:
            for token in tokens:
                if token == "1":
                    bin1 += 1
                elif token == "0":
                    bin0 += 1
                elif token == "2":
                    if bin1 == 1:
                        if bin0 == 2:
                            print("a", end="")
                    elif bin1 == 2:
                        if bin0 == 1:
                            print("b", end="")
                    elif bin1 == 5:
                        if bin0 == 3:
                            print("c", end="")
                    elif bin1 == 3:
                        if bin0 == 3:
                            print("d", end="")
                    elif bin1 == 4:
                        if bin0 == 1:
                            print("e", end="")
                    elif bin1 == 6:
                        if bin0 == 2:
                            print("f", end="")
                    elif bin1 == 7:
                        if bin0 == 1:
                            print("g", end="")
                        elif bin0 == 2:
                            print("h", end="")
                    elif bin1 == 8:
                        if bin0 == 3:
                            print("i", end="")
                        elif bin0 == 5:
                            print("j", end="")
                        elif bin0 == 6:
                            print("k", end="")
                    elif bin1 == 9:
                        if bin0 == 6:
                            print("l", end="")
                        elif bin0 == 3:
                            print("m", end="")
                        elif bin0 == 2:
                            print("n", end="")
                        elif bin0 == 5:
                            print("o", end="")
                    elif bin1 == 10:
                        if bin0 == 1:
                            print("p", end="")
                        elif bin0 == 2:
                            print("q", end="")
                        elif bin0 == 3:
                            print("r", end="")
                        elif bin0 == 4:
                            print("s", end="")
                    elif bin1 == 11:
                        if bin0 == 2:
                            print("t", end="")
                        elif bin0 == 3:
                            print("u", end="")
                        elif bin0 == 4:
                            print("v", end="")
                        elif bin0 == 5:
                            print("w", end="")
                    elif bin1 == 12:
                        if bin0 == 1:
                            print("x", end="")
                        elif bin0 == 3:
                            print("y", end="")
                        elif bin0 == 6:
                            print("z", end="")
                    elif bin1 == 13:
                        if bin0 == 1:
                            print(" ", end="")
                        elif bin0 == 2:
                            print("")
                        elif bin0 == 3:
                            print("!", end="")
                        elif bin0 == 4:
                            print("?", end="")
                        elif bin0 == 5:
                            print(".", end="")
                        elif bin0 == 6:
                            print("*", end="")
                        elif bin0 == 7:
                            print("\"", end="")
                        elif bin0 == 8:
                            print("'", end="")
                        elif bin0 == 9:
                            print("+", end="")
                        elif bin0 == 10:
                            print("-", end="")
                    elif bin1 == 14:
                        if bin0 == 1:
                            print("/", end="")
                    bin0 = 0
                    bin1 = 0

if __name__ == "__main__":
    version = "1.9"
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <command>")
        print("""commands:
-v                  shows the lang version
<file>              executes your file""")
    else:
        command = sys.argv[1]
        
        if command == "-v":
            print("Esobin made by josé icaro. made with: python")
            print(f"esobin version: {version}")
        else:
            if command.endswith(".ebin"):
                with open(command, "r") as f:
                    interpret(f.read())
            else:
                print("Use .ebin file extension!")
