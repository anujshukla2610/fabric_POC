CREATE TABLE [dbo].[fact_sales] (
    [sale_id]       BIGINT         NULL,
    [customer_id]   VARCHAR (8000) NULL,
    [product_id]    VARCHAR (8000) NULL,
    [sale_date]     DATE           NULL,
    [quantity]      BIGINT         NULL,
    [unit_price]    BIGINT         NULL,
    [amount]        BIGINT         NULL,
    [plant_name]    VARCHAR (8000) NULL,
    [inserted_dttm] DATETIME2 (6)  NULL
);


GO