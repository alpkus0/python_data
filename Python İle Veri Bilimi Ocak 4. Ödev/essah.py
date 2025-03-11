my_num_list = []


def big_and_small():
    for i in range(1, 6):  # 5 sayı almak için döngü oluşturduk
        num = int(input(f"{i}. Sayınız = "))
        my_num_list.append(num)

    print(f"\nSayıların En büyüğü: {max(my_num_list)}")
    print(f"Sayıların En küçüğü: {min(my_num_list)}")


big_and_small()
