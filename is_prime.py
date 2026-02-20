def prime(num):
    if type(num) != int or num == 1 or num == 0:
        return False
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True

if __name__ == "__main__":
    print("Please do not use this program in this way.")