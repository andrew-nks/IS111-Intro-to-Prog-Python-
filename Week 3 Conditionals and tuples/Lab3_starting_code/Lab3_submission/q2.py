## Q2 PART 1
# These variables are defined for you to use.
MEMBER_DISCOUNT_RATE = 0.10
SALE_ITEM_DISCOUNT_RATE = 0.05

# This function is for you to implement!
def calculate_price(orig_price, is_member, is_on_sale):
    
    # ################################################################################
    # Modify the code below to return the correct discounted price.
    if is_on_sale == 'yes':
        if is_member == 'yes':
            return orig_price - (orig_price * MEMBER_DISCOUNT_RATE) - (orig_price * SALE_ITEM_DISCOUNT_RATE) 
        else:
            return orig_price - (orig_price * SALE_ITEM_DISCOUNT_RATE)
    else:
        if is_member == 'yes':
            return orig_price - (orig_price * MEMBER_DISCOUNT_RATE)
        else:
            return orig_price 
    # ################################################################################

## Q2 PART 2
# Write your code below to prompt the user for the following information: 
# (1) The original price of the item. 
# (2) Whether the user is a member or not. 
# (3) Whether the item is on sale or not.:
orig_price = float(input("What's the original price of the item: $ "))
is_member = str(input("Are you a member [yes][no]? "))
is_on_sale = str(input("Is the item on sale [yes][no]? "))

print(f"The final price of the item is ${calculate_price(orig_price, is_member, is_on_sale)}")


