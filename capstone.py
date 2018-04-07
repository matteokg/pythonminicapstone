import markovify


def makeSong(text_model):
    #prints out song in style Verse1, Chorus, Verse2 using markovify text model made inside song functions.
    print('')
    print("Verse1")
    print('')
    for i in range(16):
        print(text_model.make_short_sentence(40))
    print('')
    print("Chorus")
    print('')
    for i in range(4):
        print(text_model.make_short_sentence(40))
    print('')
    print("Verse2")
    print('')
    for i in range(8):
        print(text_model.make_short_sentence(40))


def Sad():
    with open("sad.txt") as f:
        text = f.read()
        text_model = markovify.NewlineText(text)
        makeSong(text_model)


def Happy():
    with open("happy.txt") as f:
        text = f.read()
        text_model = markovify.NewlineText(text)
        makeSong(text_model)


def Angry():
    with open("angry.txt") as f:
        text = f.read()
        text_model = markovify.NewlineText(text)
        makeSong(text_model)


def TurnUp():
    with open("turnup.txt") as f:
        text = f.read()
        text_model = markovify.NewlineText(text)
        makeSong(text_model)


def printSongName(songname, ui):
    print("-----")
    print('')
    print("here is your", ui, " Drake song", "/", songname)
    print('')
    print("-----")


if __name__ == "__main__":
    print('')
    print("welcome to drake song generator v1")

    while True:
        print('')
        songname = input("name ur trake:").upper()
        print('')
        print("cool, how would you like your Drake cooked today?")
        print('')
        ui = input("please select an emotion: Sad, happy, angry or turnt?").upper()
        if ui == "SAD":
            printSongName(songname, ui)
            Sad()
        if ui == "HAPPY":
            printSongName(songname, ui)
            Happy()
        if ui == "ANGRY":
            printSongName(songname, ui)
            Angry()
        if ui == "TURNT":
            printSongName(songname, ui)
            TurnUp()
        while True:
            print('')
            again = input("want to make another one? (y)es or (n)o?").strip().lower()
            if again in ["yes", "y", 'no', 'n']:
                break
        if again in ["no", "n"]:
            print('')
            print('fine jabroni, cya in the 6')
            print('')
            break
