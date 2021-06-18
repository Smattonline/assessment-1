# Write your solution here!

# create an array of currency denominations

denominations = {
    '$100 bill': 100.00,
    '$50 bill': 50.00,
    '$20 bill': 20.00,
    '$10 bill': 10.00,
    '$5 bill': 5.00,
    '$1 bill': 1.00,
    'quarter': 0.25,
    'dime': 0.10,
    'nickel': 0.05,
    'penny': 0.01
    }

def my_optimal_change(item_cost, amount_paid):
    
    #create a variable that subtract item cost from amount paid
    change = amount_paid - item_cost
    total_change = float(round(change, 2))
    #create an empty list that will hold a list of denominations of change received
    optimal_change = []
   
    
        
   #loop through the denomination dict
    for amount in denominations:
        #create a loop that check if one of the denomination amount is less than or equal to the remaining change
        while denominations[amount] <= (total_change + 0.001):
            #append the denomination to the empty list
            optimal_change.append(amount)
            #subtract the denomination that was appended from the remaining change
            total_change -= denominations[amount]
            
    #create a dict with a count of the denominations is the list variable
    count = {i:optimal_change.count(i) for i in optimal_change}
    #create a variable that will hold a list of counts and the denominations as a string
        #denominations in the list should be changed to plural if the count is greater than 1
    new_count = []

    #loop through the count dict
    for each_count in count:
        #create a variable that stores every iteration of the count dict
        iterate = each_count
        #change every denominations in the list that has a count greater than 1 to plural, then append to the list
        #or just append the denomination if the count is 1
        if count[iterate] > 1:
            iterate = iterate.replace("bill", "bills")
            iterate = iterate.replace("quarter", "quarters")
            iterate = iterate.replace("dime", "dimes")
            iterate = iterate.replace("nickel", "nickels")
            iterate = iterate.replace("penny", "pennies")
            new_count.append(f"{count[each_count]} {iterate}")
        else:
            iterate = each_count
            new_count.append(f"{count[each_count]} {iterate}")

    #create a variable that holds a poped last element of the list
    new_count_pop = ''
    #create a variable that holds a joined remaining elements in the list into a string
    new_count_amend = ''

    # write an if statement that pops and joins only when the count list is not empty.
    if len(new_count) > 2:
         new_count_pop = new_count.pop()
         new_count_amend = ', '.join(new_count)
    elif len(new_count) == 2:
        new_count_pop = new_count[1]
        new_count_amend = new_count[0]

    #print the denominations of the change that will be given to the customer or no change if the customer paid less than or exactly the cost of the item
    if len(new_count) < 1:
        return "This customer gets no change."
    elif len(new_count) == 1:
        return f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is {new_count[0]}."
    else:
        return f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is {new_count_amend}, and {new_count_pop}."


# my_optimal_change(62.13, 100)
# my_optimal_change(31.51, 50)
# my_optimal_change(25.19, 100)
