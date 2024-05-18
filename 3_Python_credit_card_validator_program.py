#Python credit card validator program
#1. Remove any '-' or ' '
#2. Add all digits in the odd places from right to left
#3. Double every second digit from right to left.
#(If result is a two-digit number,
#add the two-digit number together to get a single digit.)
#4. Sum the totals of steps 2 & 3
#5. If sum is divisible by 10, the credit card # is valid

sum_odd_digits=0
sum_even_digits=0
total=0

#step 1
card_number=input('Enter credit card number')
card_number=card_number.replace('-','')
card_number=card_number.replace('','')
#print(card_number)
card_number=card_number[::-1]
#print(card_number)

#step 2
for num in card_number[::2]:
  sum_odd_digits+=int(num)

#step 3
for num in card_number[1::2]:
  num=int(num)*2
  if num >= 10:
    sum_even_digits+=(1+(num%10))
  else:
    sum_even_digits+=num

#step 4
total=sum_even_digits+sum_odd_digits

#step 5
if total%10==0:
  print('VALID')
else:
  print('INVALID')

