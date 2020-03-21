str_input = input("태어난 해를 입력해주세요> ")
birth_input = int(str_input) % 12

if birth_input == 0:
    print("원숭이 띠입니다.")
elif birth_input == 1:
    print("닭 띠입니다.")
elif birth_input == 2:
    print("개 띠입니다.")
elif birth_input == 3:
    print("돼지 띠입니다.")
elif birth_input == 4:
    print("쥐 띠입니다.")
elif birth_input == 5:
    print("소 띠입니다.")
elif birth_input == 6:
    print("범 띠입니다.")
elif birth_input == 7:
    print("토끼 띠입니다.")
elif birth_input == 8:
    print("용 띠입니다.")
elif birth_input == 9:
    print("뱀 띠입니다.")
elif birth_input == 10:
    print("말 띠입니다.")
elif birth_input == 11:
    print("양 띠입니다.")

birth_list = ["원숭이", "닭", "개", "돼지", "쥐", "소", "범", "토끼", "용", "뱀", "말", "양"]
str_input = input("태어난 해를 입력해주세요> ")
birth_input = int(str_input) % 12
print(f"{birth_list[birth_input]} 띠입니다.")


def birth(x):
    return {0: "원숭이", 1: "닭", 2: "개", 3: "돼지", 4: "쥐", 5: "소", 6: "범",
            7: "토끼", 8: "용", 9: "뱀", 10: "말", 11: "양"}\
        .get(x, "error")


str_input = input("태어난 해를 입력해주세요> ")
birth_input = int(str_input) % 12
print(f"{birth(birth_input)} 띠입니다.")
