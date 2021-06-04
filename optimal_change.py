# Write your solution here!

denominations = {
    100: '$100 bill',
    50: '$50 bill',
    20: '$20 bill',
    10: '$10 bill',
    5: '$5 bill',
    1: '$1 bill',
    0.25: 'quarter',
    0.10: 'dime',
    0.01: 'penny',
    }

def my_optimal_change(item_cost, amount_paid):
    
    total_change = amount_paid - item_cost
    optimal_change = []
   
    for amount in denominations:
        while total_change >= amount:
            optimal_change.append(denominations[amount])
            total_change -= amount
    
    count = {i:optimal_change.count(i) for i in optimal_change}
    new_count = []
    
    if count['penny']:
        count['penny'] += 1

    for each_count in count:
        iterate = each_count
        if count[each_count] >= 2:
            iterate = iterate.replace("bill", "bills")
            iterate = iterate.replace("quarter", "quarters")
            iterate = iterate.replace("penny", "pennies")
            iterate = iterate.replace("dime", "dimes")
            new_count.append(f"{count[each_count]} {iterate}")
        else:
            iterate = each_count
            new_count.append(f"{count[each_count]} {iterate}")
    slice_range = range(0, len(new_count))
    new_count_pop = new_count.pop()
    new_count_amend = ', '.join(new_count)
    
    return f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is {new_count_amend}, and {new_count_pop}."


# my_optimal_change(62.13, 100)
# my_optimal_change(31.51, 50)