while True:
    import os
    destination=str(f"{input("What would you like to name this file?")}.py")
    os.rename("text",destination)
    print("source path renamed to detination path successfully.")
    src=destination