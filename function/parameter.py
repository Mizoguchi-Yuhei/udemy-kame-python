def func(first, second, third="3"):
# def func(first, second="2", third):
    print(f"first: {first}, second: {second}, third: {third}.")


# argument <-> parameter
func("1", "2", "33")
func("1", "2")


func("1", third="3", second="2")