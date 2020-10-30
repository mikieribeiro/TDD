# the prints() in this code are used for visual explanatory purposes only
# Test Driven Development tests should't print anything else but the number
# of tests made, time taken and success

def hello_world() -> str:
    return 'hello world'


def get_order() -> str:
    with open("/Users/mikieribeiro/Documents/TDD/Mocked_dump.txt", "r") as dump_file:
        order = ""
        for line in dump_file:
            if "Order1" in line:
                order = line.split("=")[1].strip()
    if order:
        print(order)
        return str(order)
    else:
        return None


def is_order_valid(order: str) -> bool:
    if order:
        split_order = order.split(",")
        if len(split_order) == 15:
            for i in range(len(split_order)):
                if not 0 <= int(split_order[i]) < 15:
                    print("order is invalid")
                    return False
            print("order is valid")
            return True
    return False
