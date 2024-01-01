from Main import Run

while True:
    text = input("PyLang -> ")
    result, error = Run.run('<input>', text)

    if error:
        print(error.as_string())
    else:
        print(result)
