SELECT HISTORY_ID, 
CASE WHEN DISCOUNT_RATE IS NULL THEN (DAILY_FEE * (DATEDIFF(END_DATE, START_DATE) + 1))
ELSE FLOOR((DAILY_FEE * (DATEDIFF(END_DATE, START_DATE)+1) * ((100-DISCOUNT_RATE)/100))) END AS FEE
FROM
(SELECT HISTORY_ID, DURATION_TYPE, CAR_TYPE, DAILY_FEE, END_DATE, START_DATE FROM
(SELECT HISTORY_ID, CAR_ID, END_DATE, START_DATE,
CASE WHEN DATEDIFF(END_DATE, START_DATE)+1 >= 7 AND DATEDIFF(END_DATE, START_DATE)+1< 30 THEN '7일 이상'
WHEN DATEDIFF(END_DATE, START_DATE)+1>= 30 AND DATEDIFF(END_DATE, START_DATE)+1< 90 THEN '30일 이상'
WHEN DATEDIFF(END_DATE, START_DATE)+1>= 90 THEN '90일 이상'
ELSE 'N' END AS DURATION_TYPE FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) AS H
INNER JOIN
CAR_RENTAL_COMPANY_CAR AS C ON H.CAR_ID = C.CAR_ID) AS HC
LEFT JOIN
CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS C ON HC.CAR_TYPE = C.CAR_TYPE AND HC.DURATION_TYPE = C.DURATION_TYPE
WHERE HC.CAR_TYPE = '트럭'
ORDER BY FEE DESC, HISTORY_ID DESC
