#print(input("describe your mood in emoticon: ").replace(":)", "🙂").replace(":(", "🙁"))


def main():
    face = input("describe your mood in emoticon: ")
    print(convert(face))

def convert(x):
    face = x.replace(":)", "🙂").replace(":(", "🙁")
    return face

main()


'''
face = input("describe your mood in emoticon: ")
if ":)" in face:
    print(face.replace(":)", "🙂"))
else:
    print(face.replace(":(", "🙁"))
'''
