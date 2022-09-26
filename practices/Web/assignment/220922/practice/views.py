from django.shortcuts import render
import random

# Create your views here.

def todaydinner(request):

    favor = ['냉동삼겹살', '제주흑돼지', '양고기살치살']
    random_favor = random.choice(favor)

    if random_favor == '냉동삼겹살':
        random_imgs = 'https://www.meconomynews.com/news/photo/202102/50208_57997_421.jpeg'
    elif random_favor == '제주흑돼지':
        random_imgs = 'https://api.cdn.visitjeju.net/photomng/imgpath/202111/03/a69e833b-9bfd-42bf-89d2-6dacf80d9a33.jpg'
    else:
        random_imgs = 'http://www.ichiryu.kr/bizdemo46662/component/board/board_15/u_image/3/477429243_mainmenu3.jpg'

    context = {
        'menu': random_favor,
        'imgs': random_imgs
    }

    return render(request, 'today-dinner.html', context)


def lotto(request):

    names = ['금수저', '만수르', '건물주', '불로소득', '이 구역의 주인공은 나']
    random_name = random.choice(names)

    context = {
        'name': random_name,
    }

    return render(request, 'lotto.html', context)