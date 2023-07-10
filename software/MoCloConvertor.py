def main():
    print("What type of part is it (1-4)? fuck")
    print("Options include: (1) Promoter, (2) RBS, (3) CDS, or (4) Terminator")
    key = False
    choice = -1
    while not key:
        try:
            option = input()
            choice = int(option)
            if choice <= 4 and choice >= 1:
                key = True
            else:
                raise Exception("Out of bounds")
        except:
            print("Your input is out of bounds: it needs to be a number between 1-4")
            print("\nTry again:\n")
    if choice == 1:
        product = promoter()
    elif choice == 2:
        product = rbs()
    elif choice == 3:
        product = cds()
    elif choice == 4:
        product = term()
    print("This is your MoClo part: ")
    print(product)
#hello

def promoter():
    print("Enter your Sequence (Promoter): ")
    seq = input()
    return "atgcatgcGAAGACAActcaGGAG" + seq + "TACTcgagaagtcttcATGCATGC"

def rbs():
    print("Enter your Sequence (RBS): ")
    seq = input()
    return "atgcatgcGAAGACAActcaTACT" + seq + "AATGcgagaagtcttcATGCATGC"

def cds():
    seq = input("Enter your Sequence (CDS): ")
    return "atgcatgcGAAGACAActcaAATG" + seq + "GCTTcgagaagtcttcATGCATGC"

def term():
    seq = input("Enter your Sequence (Terminator): ")
    return "atgcatgcGAAGACAActcaGCTT" + seq + "CGCTcgagaagtcttcATGCATGC"

main()
