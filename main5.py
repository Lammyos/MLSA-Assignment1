# Credit card validation

card_num = input("Enter your credit card digits: ")
card_num = card_num[::-1]

doub_list = []
for num in card_num[1:]:
    doub = int(num) * 2
    if doub > 9:
        doub = doub - 9
    doub_list.append(int(card_num[0]))
    doub_list.append(doub)

result = sum(doub_list)
if result % 10 == 0:
    print("The Credit card number is valid.")
else:
    print("The Credit card number is invalid.")


    