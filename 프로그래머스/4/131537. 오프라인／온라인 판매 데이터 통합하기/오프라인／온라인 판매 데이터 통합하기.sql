-- 코드를 입력하세요
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT FROM
(SELECT ONLINE_SALE_ID, NULL AS OFFLINE_SALE_ID, USER_ID, PRODUCT_ID, SALES_AMOUNT, SALES_DATE FROM ONLINE_SALE
UNION ALL
SELECT NULL AS ONLINE_SALE_ID, OFFLINE_SALE_ID, NULL AS USER_ID, PRODUCT_ID, SALES_AMOUNT, SALES_DATE FROM OFFLINE_SALE) AS T1
WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 3
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID