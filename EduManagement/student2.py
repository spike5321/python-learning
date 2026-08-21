# 学生类
class Student2:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        sum = self.chinese + self.math + self.english
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{sum}"

    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


# 教务管理系统类
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []  # 列表，记录在校学生的成绩信息

    # 添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名：")

        for s in self.student_list:
            if s.name == name:
                print("该学生已存在")
                return

        chinese = int(input("请输入语文成绩："))
        math = int(input("请输入数学成绩："))
        english = int(input("请输入英语成绩："))

        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student2(name, chinese, math, english)
            self.student_list.append(stu)
            print("添加成功")
        else:
            print("成绩必须在 0~100 之间")

    # 修改学生成绩
    def update_student(self):
        name = input("请输入要修改的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩：{s}")

                chinese = int(input("请输入修改后的语文成绩："))
                math = int(input("请输入修改后的数学成绩："))
                english = int(input("请输入修改后的英语成绩："))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print("修改成功")
                    print(f"修改后的成绩：{s}")
                    return
                else:
                    print("成绩必须在 0~100 之间")
                    return
        print("该学生不存在")

    # 删除学生成绩
    def delete_student(self):
        name = input("请输入要删除的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("删除成功")
                return
        print("该学生不存在")

    # 查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息:{s}")
                return
        print("该学生不存在")

    # 展示全部学生成绩
    def show_all_students(self):
        for s in self.student_list:
            print(s)

    # 运行系统
    def run(self):
        try:
            while True:
                print("欢迎使用", self.system_name, "V", self.system_version)
                print("1. 添加学生成绩")
                print("2. 修改学生成绩")
                print("3. 删除学生成绩")
                print("4. 查询学生成绩")
                print("5. 展示全部学生成绩")
                print("6. 退出系统")
                choice = input("请输入你的选择：")
                if choice == "1":
                    self.add_student()
                elif choice == "2":
                    self.update_student()
                elif choice == "3":
                    self.delete_student()
                elif choice == "4":
                    self.query_student()
                elif choice == "5":
                    self.show_all_students()
                elif choice == "6":
                    print("感谢使用", self.system_name, "V", self.system_version)
                    break
                else:
                    print("无效的选择，请重新输入")
        except ValueError:
            print("输入错误，请重新输入")
        except Exception:
            print("发生错误，请重新输入")

# 测试
if __name__ == '__main__':
    edum = EduManagement()
    edum.run()
