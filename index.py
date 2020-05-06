import speech_recognition as sr
import maths
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source)
    print("Stopped listening")

if r.recognize_google(audio) == "Maths":
    try:
        with sr.Microphone() as source:
            print("Say something")
            audio = r.listen(source)
            print("Stopped listening")
        text = r.recognize_google(audio)
        print("QUESTION: "+ text)
        s = text.split()
        if set(["add", "addition"]) & set(s):
            maths.Maths.addition(s)
        elif set(["sub", "subraction"]) & set(s):
            maths.Maths.subraction(s)
        elif set(["multiply", "multiplication"]) & set(s):
            maths.Maths.multiplication(s)
        elif set(["divide", "division"]) & set(s):
            maths.Maths.division(s)
        else:
            print("Speak Again")

    except:
        print("end with some error")

elif r.recognize_google(audio) == "database":
    import pandas as pd
    import dataframes as dframe
    try:
        df = pd.read_csv("batsmenscore.csv")
        with sr.Microphone() as source:
            print("Now start asking queries the from the data set")
            audio = r.listen(source)
            print("Stopped listening")
        text = r.recognize_google(audio)
        text = text.split()
        if set(["top", "first", "rows"]) & set(text) & set(["rows"]):
            rows = maths.Maths.getNumber(text)
            dframe.Display.toprows(df, rows)

        elif set(["top", "first", "columns"]) & set(text) & set(["columns"]):
            columns = maths.Maths.getNumber(text)
            dframe.Display.firstcolumns(df, columns)

    except:
        print("error while accessing databases")
else:
    print("No such Module found")



