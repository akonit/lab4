use PRODUCTS;

INSERT INTO products_product (id, name, description, mark, voters)
VALUES (1, 'тестовый продукт 1', 'описание1', 3.4, 8);

INSERT INTO products_opinion (id, product_id, login, text, pub_date)
VALUES (1, 1, 'me', 'nothing outstanding here', SYSDATE());

INSERT INTO products_category(id, name)
VALUES (1, 'тестовая категория');

INSERT INTO products_product_categories(id, product_id, category_id)
VALUES (1, 1, 1);
