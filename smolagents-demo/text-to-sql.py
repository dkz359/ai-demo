from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    Float,
    ForeignKey,
    insert,
    inspect,
    text,
)
from smolagents import tool, CodeAgent, LiteLLMModel

# 创建内存数据库
engine = create_engine("sqlite:///:memory:")
metadata_obj = MetaData()

# 创建商品表
products = Table(
    "products",
    metadata_obj,
    Column("product_id", Integer, primary_key=True),
    Column("product_name", String(50), nullable=False),
    Column("category", String(20)),
    Column("unit_price", Float, nullable=False),
    Column("stock_quantity", Integer, nullable=False),
)

# 创建订单表
orders = Table(
    "orders",
    metadata_obj,
    Column("order_id", Integer, primary_key=True),
    Column("product_id", Integer, ForeignKey("products.product_id")),
    Column("customer_name", String(50)),
    Column("order_date", String(10)),
    Column("quantity", Integer),
    Column("total_amount", Float),
)

metadata_obj.create_all(engine)

# 插入示例商品数据
product_data = [
    {"product_id": 1, "product_name": "iPhone 14", "category": "手机", "unit_price": 5999.0, "stock_quantity": 100},
    {"product_id": 2, "product_name": "MacBook Pro", "category": "笔记本", "unit_price": 12999.0, "stock_quantity": 50},
    {"product_id": 3, "product_name": "AirPods Pro", "category": "配件", "unit_price": 1999.0, "stock_quantity": 200},
    {"product_id": 4, "product_name": "iPad Air", "category": "平板", "unit_price": 4799.0, "stock_quantity": 80},
    {"product_id": 5, "product_name": "Apple Watch", "category": "智能手表", "unit_price": 3299.0,
     "stock_quantity": 150},
    {"product_id": 6, "product_name": "小米13", "category": "手机", "unit_price": 3999.0, "stock_quantity": 120},
    {"product_id": 7, "product_name": "华为Mate60", "category": "手机", "unit_price": 6999.0, "stock_quantity": 90},
    {"product_id": 8, "product_name": "联想小新Pro", "category": "笔记本", "unit_price": 5999.0, "stock_quantity": 45},
    {"product_id": 9, "product_name": "华为MateBook", "category": "笔记本", "unit_price": 6599.0, "stock_quantity": 60},
    {"product_id": 10, "product_name": "小米手环", "category": "智能手表", "unit_price": 249.0, "stock_quantity": 300},
    {"product_id": 11, "product_name": "华为手表", "category": "智能手表", "unit_price": 1499.0, "stock_quantity": 180},
    {"product_id": 12, "product_name": "荣耀手机", "category": "手机", "unit_price": 2999.0, "stock_quantity": 150},
    {"product_id": 13, "product_name": "戴尔XPS", "category": "笔记本", "unit_price": 9999.0, "stock_quantity": 30},
    {"product_id": 14, "product_name": "机械键盘", "category": "配件", "unit_price": 399.0, "stock_quantity": 250},
    {"product_id": 15, "product_name": "无线鼠标", "category": "配件", "unit_price": 129.0, "stock_quantity": 400},
    {"product_id": 16, "product_name": "显示器", "category": "配件", "unit_price": 1299.0, "stock_quantity": 120},
    {"product_id": 17, "product_name": "小米平板", "category": "平板", "unit_price": 2299.0, "stock_quantity": 100},
    {"product_id": 18, "product_name": "华为平板", "category": "平板", "unit_price": 3599.0, "stock_quantity": 85},
    {"product_id": 19, "product_name": "蓝牙耳机", "category": "配件", "unit_price": 499.0, "stock_quantity": 300},
    {"product_id": 20, "product_name": "手机壳", "category": "配件", "unit_price": 49.0, "stock_quantity": 1000},
    {"product_id": 21, "product_name": "充电器", "category": "配件", "unit_price": 129.0, "stock_quantity": 800},
    {"product_id": 22, "product_name": "移动电源", "category": "配件", "unit_price": 199.0, "stock_quantity": 600},
    {"product_id": 23, "product_name": "ThinkPad", "category": "笔记本", "unit_price": 8999.0, "stock_quantity": 40},
]

for row in product_data:
    stmt = insert(products).values(**row)
    with engine.begin() as connection:
        connection.execute(stmt)

# 插入示例订单数据
order_data = [
    {"order_id": 1, "product_id": 1, "customer_name": "张三", "order_date": "2024-01-01", "quantity": 2,
     "total_amount": 11998.0},
    {"order_id": 2, "product_id": 2, "customer_name": "李四", "order_date": "2024-01-02", "quantity": 1,
     "total_amount": 12999.0},
    {"order_id": 3, "product_id": 3, "customer_name": "王五", "order_date": "2024-01-03", "quantity": 3,
     "total_amount": 5997.0},
    {"order_id": 4, "product_id": 4, "customer_name": "赵六", "order_date": "2024-01-03", "quantity": 1,
     "total_amount": 4799.0},
    {"order_id": 5, "product_id": 5, "customer_name": "钱七", "order_date": "2024-01-04", "quantity": 2,
     "total_amount": 6598.0},
    {"order_id": 6, "product_id": 1, "customer_name": "孙八", "order_date": "2024-01-04", "quantity": 1,
     "total_amount": 5999.0},
    {"order_id": 7, "product_id": 7, "customer_name": "周九", "order_date": "2024-01-05", "quantity": 1,
     "total_amount": 6999.0},
    {"order_id": 8, "product_id": 10, "customer_name": "吴十", "order_date": "2024-01-05", "quantity": 5,
     "total_amount": 1245.0},
    {"order_id": 9, "product_id": 14, "customer_name": "郑十一", "order_date": "2024-01-06", "quantity": 3,
     "total_amount": 1197.0},
    {"order_id": 10, "product_id": 6, "customer_name": "王婷婷", "order_date": "2024-01-06", "quantity": 2,
     "total_amount": 7998.0},
    {"order_id": 11, "product_id": 8, "customer_name": "李明", "order_date": "2024-01-07", "quantity": 1,
     "total_amount": 5999.0},
    {"order_id": 12, "product_id": 12, "customer_name": "张华", "order_date": "2024-01-07", "quantity": 2,
     "total_amount": 5998.0},
    {"order_id": 13, "product_id": 15, "customer_name": "刘芳", "order_date": "2024-01-08", "quantity": 4,
     "total_amount": 516.0},
    {"order_id": 14, "product_id": 17, "customer_name": "陈明", "order_date": "2024-01-08", "quantity": 1,
     "total_amount": 2299.0},
    {"order_id": 15, "product_id": 20, "customer_name": "王磊", "order_date": "2024-01-09", "quantity": 10,
     "total_amount": 490.0},
    {"order_id": 16, "product_id": 3, "customer_name": "李娜", "order_date": "2024-01-09", "quantity": 2,
     "total_amount": 3998.0},
    {"order_id": 17, "product_id": 9, "customer_name": "张伟", "order_date": "2024-01-10", "quantity": 1,
     "total_amount": 6599.0},
    {"order_id": 18, "product_id": 11, "customer_name": "王秀英", "order_date": "2024-01-10", "quantity": 2,
     "total_amount": 2998.0},
    {"order_id": 19, "product_id": 19, "customer_name": "李军", "order_date": "2024-01-11", "quantity": 3,
     "total_amount": 1497.0},
    {"order_id": 20, "product_id": 13, "customer_name": "刘洋", "order_date": "2024-01-11", "quantity": 1,
     "total_amount": 9999.0},
    {"order_id": 21, "product_id": 21, "customer_name": "张萍", "order_date": "2024-01-12", "quantity": 5,
     "total_amount": 645.0},
    {"order_id": 22, "product_id": 22, "customer_name": "王强", "order_date": "2024-01-12", "quantity": 3,
     "total_amount": 597.0},
    {"order_id": 23, "product_id": 16, "customer_name": "李艳", "order_date": "2024-01-13", "quantity": 2,
     "total_amount": 2598.0},
]

for row in order_data:
    stmt = insert(orders).values(**row)
    with engine.begin() as connection:
        connection.execute(stmt)


# 获取表结构信息
def get_table_info(table_name):
    inspector = inspect(engine)
    columns_info = [(col["name"], col["type"]) for col in inspector.get_columns(table_name)]
    return "Columns:\n" + "\n".join([f"  - {name}: {col_type}" for name, col_type in columns_info])


@tool
def sql_engine(query: str) -> str:
    """
    执行SQL查询,支持商品表(products)和订单表(orders)的联合查询。

    商品表结构:
    - product_id: INTEGER (主键)
    - product_name: VARCHAR(50)
    - category: VARCHAR(20)
    - unit_price: FLOAT
    - stock_quantity: INTEGER

    订单表结构:
    - order_id: INTEGER (主键)
    - product_id: INTEGER (外键关联products表)
    - customer_name: VARCHAR(50)
    - order_date: VARCHAR(10)
    - quantity: INTEGER
    - total_amount: FLOAT

    Args:
        query: SQL查询语句
    """
    output = ""
    with engine.connect() as con:
        rows = con.execute(text(query))
        for row in rows:
            output += "\n" + str(row)
    return output


# 创建agent实例
agent = CodeAgent(
    tools=[sql_engine],
    model=LiteLLMModel(model_id="gpt-4o-mini"),
)

# 示例查询
# print("===示例查询1: 获取销量最高的商品信息===")
# agent.run("""
# 查询销量最高的商品的详细信息,包括商品名称、销量和销售总额。
# 需要联合查询products和orders表,按订单数量统计。
# """)

# print("\n===示例查询2: 获取库存紧张的商品===")
# agent.run("""
# 查询当前库存数量低于50件的商品信息,
# 返回商品名称、类别、当前库存数量,按库存数量升序排序。
# """)

# print("===示例查询3: 各类别商品的销售统计===")
# agent.run("""
# 统计每个商品类别的总销售额和销售数量,
# 按销售总额降序排序,同时显示该类别的商品数量。
# """)

print("\n===示例查询4: 热销商品分析===")
agent.run("""
查找单价超过1000元且销量超过2件的商品,
显示商品名称、单价、销量、销售总额,
按销售总额降序排序。
""")

print("\n===示例查询5: 客户购买力分析===")
agent.run("""
统计每个客户的消费总额和购买次数,
只显示消费总额超过10000元的客户,
按消费总额降序排序。
""")

print("\n===示例查询6: 商品库存周转分析===")
agent.run("""
计算每个商品的销量与库存比率(周转率),
显示商品名称、销量、当前库存、周转率,
只显示周转率超过10%的商品,
按周转率降序排序。
""")

print("\n===示例查询7: 日销售趋势分析===")
agent.run("""
统计每天的订单数量、销售总额、平均订单金额,
按日期升序排序。
""")

