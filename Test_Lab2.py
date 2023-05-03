import ET0735_Lab2.Lab2 as Lab2

print("Test_bmi")

def test_find_min_max():
    result = []
    input_arr = [1,4,2,5,3]
    test_arr = [1,5]
    result = Lab2.find_min_max(input_arr)
    assert(result == test_arr)

def test_calc_average():
    input_arr = [1, 4, 2, 5, 3]

    result = Lab2.calc_average(input_arr)

    assert(result == 3)


def test_calc_median_tempearture_odd():
    input_arr = [1,2,3,4,5]
    result = Lab2.calc_median_temperature(input_arr)

    assert(result == 3)


def test_calc_median_tempearture_even():
    input_arr = [1,2,3,4]
    result = Lab2.calc_median_temperature(input_arr)

    assert (result == 2.5)






















