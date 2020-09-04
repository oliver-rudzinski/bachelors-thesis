--SQL
SELECT
  sequencenumber as InvoiceNo, 
  itemcategory as Description,
  SUBSTRING(itemid, 1, 1) as ItemType,
  quantity as Quantity
FROM retail_transactions
ORDER BY InvoiceNo