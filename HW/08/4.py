class DiscountError(Exception):
    pass


def apply_discount(price: int, discount: float) -> int:
    # “””This Function Calculated the Final Price”””
    result = int(price * (1 - discount))
    #1

    # try:
    #     assert 0 <= result <= price
    # except AssertionError as e:
    #     raise DiscountError(e)

    #2
    # if 0 <= result <= price :
    #     raise DiscountError("reza")
    # else:
    #     print("ok")

    #3
    try:
        assert 0 <= result <= price
    except Exception:
        raise DiscountError("DiscounError !!!!!!!!!")




print(apply_discount(10, 5))
