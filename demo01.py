def convert_usd_to_cny(usd_amount):
    cny_amount = usd_amount * 0.145
    return cny_amount

def main():
    usd_amount = float(input("Enter the dollar amount: "))
    cny_amount = convert_usd_to_cny(usd_amount)
    print("The equivalent amount in Chinese yuan is: ${}\n".format(cny_amount))

if __name__ == '__main__':
    main()