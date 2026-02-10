#using to change payment and cash amount
total_amount = float(input("Enter total amount ? :"));
cash_payment = float(input("Enter cash payment ? :"));

change_due = cash_payment - total_amount;
change_cent = round(change_due * 100);

#caculate coin
dollars = change_cent // 100;
change_cent = change_cent % 100;

quatar = change_cent // 25;
change_cent = change_cent % 25;

dims = change_cent // 10;
change_cent = change_cent * 10;

nickels = change_cent // 5;
change_cent = change_cent * 5;

pelnies = change_cent;

# result the prints
print("Change due : ", format(change_due, ".2f"))
print("Dollar : ", dollars);
print("Quatar : ", quatar);
print("Dims : ", dims);
print("Nickel : ", nickels);
print("Pelnies : ", pelnies);
