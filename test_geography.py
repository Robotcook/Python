from geography import check_guess

def test_check_guess():
    assert check_guess("Ljubljana", "Slovenia")
    return "Check Guess Passed."

print (test_check_guess())