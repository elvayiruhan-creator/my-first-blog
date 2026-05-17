import polars as pl
import random  # 老师的代码里用了这个
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel  # 必须导入这个来做数据检查

# 1. 初始化 App（全文件只能有一个 app = FastAPI()）
app = FastAPI()

# 2. 企鹅数据准备（Exercise 4 & 5）
filename = Path(__file__).parent / 'penguins.csv'
df = pl.read_csv(filename)

# 3. Pydantic 模型定义（老师新教的“数据合同”）
class House(BaseModel):
    bedrooms: int
    bathrooms: int
    sqmt_living: int

class Prediction(BaseModel):
    price: float

# --- 4. 路由部分（菜单里的各种菜） ---

# 基础测试
@app.get("/")
def read_root():
    return {"Hello": "World", "message": "Welcome to Penguin & House API!"}

# 【企鹅功能 1】：按 ID 查企鹅
@app.get("/penguins/{penguin_id}")
def get_penguin(penguin_id: int):
    selected = df.filter(id=penguin_id)
    return selected.to_dicts()

# 【企鹅功能 2】：按物种过滤企鹅
@app.get("/penguins")
def get_penguins_by_species(species: str = None):
    if species:
        filtered_df = df.filter(pl.col("species") == species)
        return filtered_df.to_dicts()
    return df.head(5).to_dicts()

# 【房价功能 1】：随机价格（老师代码第 11-13 行）
@app.get("/price/{item_id}")
def house_price(item_id: int):
    return {"item_id": item_id, "price": random.randint(100000, 500000)}

# 【房价功能 2】：房价预测（老师代码第 25-31 行）
@app.post("/predict")
def house_price_2(house: House) -> Prediction:
    # 按照老师给的公式计算
    predicted_price = house.bedrooms * 50000 + house.bathrooms * 30000 + house.sqmt_living * 200
    return Prediction(price=predicted_price)