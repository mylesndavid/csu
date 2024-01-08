
#Part 1

#ask user for input for price of food before tax
base = round(float(input("Enter the price of your meal here. Your total cost including an 18% tip and 7% tax will be calculated\nPrice: ")),2)
#calculate cost of tip and tax individually 
tip = round(base * .18,2)
tax = round(base * .07,2)
#add base price to tax and tip and store in variable 'total'
total = base + tip + tax

print(f'\nBase Price: ${base:.2f}\nTip Cost at 18%: ${tip:.2f}\nTax Cost at 7%: ${tax:.2f}\nTotal Cost: ${total:.2f}')


#Part 2 

#ask user for input for current time and then time to wait in hours
current_time = int(input('Enter the current time in 24 hour standard(no colon): '))
wait_time = int(input('Time to wait(hours): '))
alarm = (current_time + wait_time) % 24
print(f'Alarm is set for {alarm:02d}:00')