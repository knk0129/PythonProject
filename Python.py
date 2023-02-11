import navi

screen_width = 480
screen_height = 640
screen = .navi.display.set_mode((screen_width, screen_height))

navi.display.set_caption("Navigation")

navi = {}
while True:
    print("===즐겨찾기 등록===")
    print("1.주소 등록")
    print("2.주소 수정")
    print("3.주소 목록")
    print("4.검색")
    print("5.종료")
    num = int(input("번호 선택: "))
    if num == 1:
        name = input("목적지 이름을 입력해주세요: ")
        if navi.get(name) == None:
            navi[name] = input("목적지 주소를 입력하세요: ")
            print("등록 완료 되었습니다.")
        else:
            print("입력하신 목적지는 이미 존재 합니다.")
    elif num ==2:
        name = input("수정하실 목적지 이름을 입력해주세요: ")
        if navi.get(name) == None:
            print("잘못입력하셨습니다.")
        else:
            navi[name] = input("수정하실 목적지 주소를 입력하세요: ")
            print("수정 완료 되었습니다.")
    elif num == 3:
        for a,b in navi.items():
            print(a,"\t",b)
    elif num == 4:
        name = input("검색하실 목적지 이름을 입력해주세요: ")
        if navi.get(name) == None:
            print("입력하신 목적지는 존재하지 않습니다.")
        else:
            print(navi.get(name)) 
    elif num == 5:
        print("프로그램을 종료 합니다.")
        break
    else:
        print("번호를 다시 입력해주세요.")
