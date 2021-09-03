def solution(price, money, count):
    # count 를 1부터 count 까지의 합 * price 
    # money 에서 합을 제거, 한 줄로 해결이 가능하지만 직관적으로 보기위해서 변수 선언
    totalPrice = sum([i for i in range(count + 1)]) * price
    return totalPrice - money if totalPrice > money else 0