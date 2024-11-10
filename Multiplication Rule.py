def prob_a_and_b(a, b,total):
    prob_a = orange/total
    prob_bga = blue/total(total-1)
    prob_AandB = prob_a * prob_bga
    return round(prob_AandB,3)
orange = int(input("Enter No of Orange "))
blue = int(input("Enter No of Blue "))
total = orange +blue
print('Prob of Getting 1st orange and 2nd blue balls: ')
print(prob_a_and_b(orange,blue,total))    