-- 코드를 입력하세요
SELECT product_code, sum(off.sales_amount * p.price) as sales
from product p join offline_sale off
on p.product_id = off.product_id
group by p.product_code
order by sales desc, product_code asc