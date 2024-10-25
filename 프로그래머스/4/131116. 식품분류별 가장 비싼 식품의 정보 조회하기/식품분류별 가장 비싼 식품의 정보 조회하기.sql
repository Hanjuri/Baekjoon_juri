SELECT 
    fp.CATEGORY, 
    fp.PRICE AS prices, 
    fp.PRODUCT_NAME
FROM 
    FOOD_PRODUCT fp
JOIN (
    SELECT 
        CATEGORY, 
        MAX(PRICE) AS MAX_PRICE
    FROM 
        FOOD_PRODUCT
    WHERE 
        CATEGORY IN ('과자', '국', '김치', '식용유')
    GROUP BY 
        CATEGORY
) max_prices ON fp.CATEGORY = max_prices.CATEGORY 
AND fp.PRICE = max_prices.MAX_PRICE
ORDER BY 
    prices DESC;