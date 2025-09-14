name = [
    "jinesh patel",
   "  jin p",
   " JIn pat   ",
    "Nidhi D ",
    "nid d",
    "  NIdhi DUd"
]


def main():
    cleaned_name = []
    for n in name:
        cleaned_name.append(n.strip().title())
        #print(cleaned_name)
    #print(cleaned_name)
    print(', '.join(cleaned_name))


main()
