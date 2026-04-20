from logic import three_sum

def test():
    assert sorted(three_sum([-1,0,1,2,-1,-4])) == sorted([[-1,-1,2],[-1,0,1]])

test()
print("Test Passed")

