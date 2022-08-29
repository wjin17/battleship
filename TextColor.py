class TextColor:
    @staticmethod
    def red(text): return f"\033[91m{text}\033[00m"
 
    @staticmethod
    def green(text): return f"\033[92m{text}\033[00m"

    @staticmethod
    def yellow(text): return f"\033[93m{text}\033[00m"
    
    @staticmethod
    def purple(text): return f"\033[94m{text}\033[00m"
    
    #def prPurple(text): return "\033[95m {}\033[00m" .format(text))
        
    @staticmethod
    def blue(text): return f"\033[96m{text}\033[00m"

    @staticmethod
    def gray(text): return f"\033[97m{text}\033[00m"
    
    @staticmethod
    def black(text): return f"\033[98m{text}\033[00m"

if __name__ == "__main__":
    print("wtf dawg")
    print(TextColor.red("red"))
    print(TextColor.green("green"))
    print(TextColor.yellow("yellow"))
    print(TextColor.purple("purple"))
    print(TextColor.blue("blue"))
    print(TextColor.gray("gray"))
    print(TextColor.black("black"))
    print("Normal")