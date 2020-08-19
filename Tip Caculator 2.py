total_amount = float(input('Total bill amount? '))

service = input('Rate your level of service from good, fair or bad: ')
service = service.lower()


if service == 'good':
  tip_amount = total_amount * .2
elif service == 'fair':
  tip_amount = total_amount * .15
elif service == 'bad':
  tip_amount = total_amount * .1
else:
  print()  

format_tip = "%.2f" % tip_amount

format_bill = "%.2f" % total_amount

format_total_bill = float(format_tip) + float(format_bill)



print(f'Tip Amount: ${format_tip}')
print(f'Total Amount: ${format_total_bill}')

ask_to_split = str(input('Would you like to split the check? '))
if ask_to_split.lower() == 'yes':
  number_of_people = int(input('How many people? '))

   

per_person = format_total_bill / number_of_people  

print(f'Amount per person: ${per_person}')
