from openpyxl import load_workbook

load_wb = load_workbook("C:/Users/londo/OneDrive/바탕 화면/dataLap/cafe24listorg/burberry/burberry_cat.xlsx", data_only=True)
load_ws = load_wb['Sheet1']
get_cells = load_ws['M11':'M128']

for row in get_cells:
    for cell in row:
        catname = cell.value
        def cat(name):
            if '크로스' in name:
                return '145|79'
            elif '토트' in name:
                return '145|80'
            elif '버켓' in name:
                return '145|81'
            elif '백팩' in name:
                return '145|82'
            elif '파우치' in name:
                return '145|84'
            elif '가방기타' in name:
                return '145|83'
            elif '핸드폰' in name:
                return '93'
            elif '넥타이' in name:
                return '112'
            elif '선글라스' in name:
                return '99'
            elif '쥬얼리' in name:
                return '94'
            elif '헤어' in name:
                return '152'
            elif '귀걸이' in name:
                return '94'
            elif '양말' in name:
                return '98'
            elif '모자' in name:
                return '92'
            elif '장갑' in name:
                return '91'
            elif '벨트' in name:
                return '90'
            elif '카드' in name:
                return '89'
            elif '지갑S' in name:
                return '88'
            elif '지갑L' in name:
                return '87'
            elif '파우치' in name:
                return '84'
            elif '' in name:
                return '-'

        results = cat(catname)
        print(results)

크로스 145|79
토트 145|80
버켓 145|81
백팩 145|82
파우치 145|84
가방기타 145|84


귀걸이 147|94|103
기타65|152
기타146|92
넥타이 153|112
모자 147|92
백팩 145|82
범백 145|83
벨트 146|90
선글라스 146|99
숄더백 63|79
스카프 146|97
스타킹 146|94
양말 146|98
장갑 146|91

핸드폰 147|93
브로치 147|94|102
귀걸이 147|94|103
헤어 147|94|104
목걸이 147|94|105
반지 147|94|106
팔찌 147|94|107

체인 146|86
지갑L 146|87
지갑S 146|88
카드  146|89









