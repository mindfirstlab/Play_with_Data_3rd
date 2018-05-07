station_addreess = ['대한민국 서울특별시 중구 을지로동 수표로 27',
                    '대한민국 서울특별시 종로구 종로1.2.3.4가동 율곡로 46',
                    '대한민국 서울특별시 중구 남대문로5가 한강대로 410',
                    '대한민국 서울특별시 서대문구 미근동 통일로 113',
                    '대한민국 서울특별시 종로구 종로1.2.3.4가동 창경궁로 112-16',
                    '대한민국 서울특별시 용산구 원효로1가 12-12',
                    '대한민국 서울특별시 성북구 삼선동5가 301',
                    '대한민국 서울특별시 동대문구 청량리동 약령시로21길 29',
                    '대한민국 서울특별시 마포구 아현동 618-1',
                    '대한민국 서울특별시 영등포구 당산동3가 2-11',
                    '대한민국 서울특별시 성동구 행당1동 왕십리광장로 9',
                    '대한민국 서울특별시 동작구 노량진동 72',
                    '대한민국 서울특별시 광진구 구의1동 자양로 167',
                    '대한민국 서울특별시 은평구 대조동 통일로 757',
                    '대한민국 서울특별시 강북구 번1동 415-15',
                    '대한민국 서울특별시 관악구 신림동 544',
                    '대한민국 서울특별시 중랑구 신내1동 신내역로3길 40-10',
                    '대한민국 서울특별시 강남구 대치동 998',
                    '대한민국 서울특별시 관악구 봉천동',
                    '대한민국 서울특별시 양천구 신월동 화곡로 73',
                    '대한민국 서울특별시 강동구 성내1동 성내로 57',
                    '대한민국 서울특별시 성북구 종암동 종암로 135',
                    '대한민국 서울특별시 구로구 가마산로 235',
                    '대한민국 서울특별시 서초구 서초3동 반포대로 179',
                    '대한민국 서울특별시 양천구 신정6동 목동동로 99',
                    '대한민국 서울특별시 송파구 가락본동 9',
                    '대한민국 서울특별시 노원구 하계동 노원로 283',
                    '대한민국 서울특별시 서초구 방배2동 동작대로 204',
                    '대한민국 서울특별시 은평구 불광2동 연서로 365',
                    '대한민국 서울특별시 도봉구 창4동 노해로 403',
                    '대한민국 서울특별시 강남구 개포동 개포로 617']

gu_name = []

# for name in station_addreess:
#     # 모든 주소의 공백을 기준으로 리스트를 형태로 뽑아냄 ex> [str,,,,]
#     tmp = name.split()
#     # 주소에서 '강'으로 시작하는 주소를 찾아내서 별도의 리스트에 저장
#     for gu in tmp:
#         if gu[0] == '강':
#             gu_name.append(gu)


# 위의 소스를 간결하게 처리하도록 수정
for name in station_addreess:
    tmp = name.split()
    # 리스트형태로 반환이 되기 때문에 뒤에 인덱스를 줘서 item을 반환하는 형식으로 처리
    tmp_gu = [gu for gu in tmp if gu[-1] == '구'][0]
    gu_name.append(tmp_gu)

