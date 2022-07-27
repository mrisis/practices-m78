import pickle


def calculate_division(file_path:str):
    file=open(file_path,"rb")
    numbers=pickle.load("numbers.pickle")

    try:
        result=list(map(lambda t: [0] / t[1],numbers))
    except TypeError:
        result=[None for _ in numbers]
    except ZeroDivisionError:
        print("is not divede by zero")
    finally:
        file.close()
        return result





