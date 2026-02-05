def threshold_checker(threshold):
    def check(value):
        if value < threshold:
            return False
        else:
            return True
    return(check)

# Usage
greater_than_10 = threshold_checker(10)
print(greater_than_10(12))
print(greater_than_10(8))