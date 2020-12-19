## 백준 코딩 테스트 문제 매일 도전하기
2020.10~

* day6 : 2742, 11021, 11022

    새로 배운 지식

    map(func, iter)

    formatting: print('Cases #%d'%(i))

* day7 : 2438, 2439, 10871
    새로 배운 지식
    print(end =" ")

    정렬은 띄어쓰기로.

* day8 : 10952, 10951, 1110
    새로 배운 지식

    몫은 //
    나머지는 %

    str처리보다 숫자 그대로 사용이 좋다 
    EOF를 위해 while + try ~ except

* day9 : 10818, 2562, 2577
    새로 배운 지식

    list의 index는 list.index(value)

    문자 배열의 각 원소를 카운팅해주는 함수는 str.count(i)

* day10 : 3052, 1546, 8958
    새로 배운 지식

    list의 distinct value만 추릴 때는 set함수 이용하기!

    [3*x for x in [111, 222, 333]] list looping

* day11-12 : 4344, 15596, 4673

    list comprehension if else를 다시 익혔다.

    [1 if x> avg else 0 for x in case]

    format(a, '.2f') 소수점 둘째자리까지 나타내라

    숫자의 자리수를 구하기 위해서 //와 %을 사용할 것!!!

    sorted(ans)는 ans.sorted()이렇게 사용 불가!

* day 13 : 1056, 11654, 11720

    int형 숫자를 자리수로 나누기 위한 방법: list(map(int, str(n)))

    등차 수열 아이디어 : a, b, c일때, b-a = c-b

    ord()함수는 아스키 코드를 불러오는 내장 함수

    chr()함수와 반대이다.

* day 14 : 11720, 10809, 2675

    소문자 알파벳을 불러오는 법

      1. string.ascii_lowercase

      2. map(chr, range(97, 123)) -> 아스키 코드 번호

    숏코딩은 정말 어렵다 ㅠ

    문자열을 찾을때는 find함수를 사용할것

    문자열도 int형처럼 계산이 된다는 성질

    R, S = input().split()처럼 튜플의 성질을 이용해서 복수개의 object 할당 가능하다는 것(오랜만에 파이썬을 해서 잊었음..)
