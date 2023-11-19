def guide():
    #Get the inputs from user, 
    num_guides = int(input("Enter the number of guides selling cookies: "))
    list = []
    for i in range(1, num_guides + 1):
        name = input(f"Enter name of Guide {i}: ")
        boxes_sold = int(input(f"Enter the number of boxes sold by {name}: "))
        list.append((name, boxes_sold))
    return list

def calculate_avg(list):
    total_boxes_sold = sum(boxes_sold for _, boxes_sold in list)
    avg_sales = total_boxes_sold / len(list)
    return avg_sales

def print_guide_prize(list, avg_sales):
    print("\nGuide List and Prizes:")
    for name, boxes_sold in list:
        if boxes_sold == 0:
            prize = ""
        elif boxes_sold > avg_sales:
            prize = "Badge"
        else:
            prize = "Left over cookies"
        print(f"{name}: {prize}")


def main():
    list = guide()
    avg_sales = calculate_avg(list)
    print_guide_prize(list, avg_sales)

if __name__ == "__main__":
    main()