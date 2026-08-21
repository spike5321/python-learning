# 商品类
class Goods:
    def __init__(self, name, price , num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称：{self.name} | 商品价格：{self.price} | 商品数量：{self.num}"

    def update_num(self, num):
        if num < 0:
            print("数量不能为负数")
            return
        self.num = num
        return

    def update_price(self, price):
        if price < 0:
            print("价格不能为负数")
            return
        self.price = price
        return

# 系统类
class System:
    system_version = "1.0.0"
    system_name = "购物车系统"
    # 系统初始化
    def __init__(self):
        self.goods_list = []

    # 添加商品
    def add_goods(self):
        name = input("请输入商品名称：")

        for goods in self.goods_list:
            if goods.name == name:
                print("商品已存在")
                return

        price = float(input("请输入商品价格："))
        num = int(input("请输入商品数量："))

        if price < 0 or num < 0:
            print("价格和数量不能为负数")
            return


        goods = Goods(name, price, num)
        self.goods_list.append(goods)
        print(f"添加商品：{goods.name} 成功")
        return

    # 修改商品
    def update_goods(self):
        name = input("请输入商品名称：")
        for goods in self.goods_list:
            if goods.name == name:
                print(f"{goods.name} 的价格为 {goods.price}, 数量为 {goods.num}")

                price = float(input("请输入商品价格："))
                num = int(input("请输入商品数量："))

            if price < 0 or num < 0:
                print("价格和数量不能为负数")
                return

            goods.update_price(price)
            goods.update_num(num)
            print(f"修改商品：{goods.name} 成功")
            return
        print("商品不存在")

    # 删除商品
    def delete_goods(self):
        name = input("请输入商品名称：")
        for goods in self.goods_list:
            if goods.name == name:
                self.goods_list.remove(goods)
                print(f"删除商品：{goods.name} 成功")
                return
        print("商品不存在")


    # 查询商品
    def query_goods(self):
        name = input("请输入商品名称：")
        for goods in self.goods_list:
            if goods.name == name:
                print(f"商品名称：{goods.name} 商品价格： {goods.price}, 商品数量： {goods.num}")
                return
        print("商品不存在")

    #运行系统
    def run(self):
        while True:
            print("欢迎使用", self.system_name, "V", self.system_version)
            print("1. 添加商品")
            print("2. 修改商品")
            print("3. 删除商品")
            print("4. 查询商品")
            print("5. 退出系统")
            choice = input("请输入你的选择：")
            if choice == "1":
                self.add_goods()
            elif choice == "2":
                self.update_goods()
            elif choice == "3":
                self.delete_goods()
            elif choice == "4":
                self.query_goods()
            elif choice == "5":
                print("退出系统")
                break
            else:
                print("输入错误")

#测试
if __name__ == "__main__":
    system = System()
    system.run()


