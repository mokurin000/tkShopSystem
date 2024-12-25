import tkinter as tk
from functools import partial
from tkinter import messagebox

from tkshopsystem.auth import check_login_hn
from tkshopsystem.const import (
    BACKGROUND_COLOR,
    BUTTON_COLOR,
    BUTTON_TEXT_COLOR,
    LABEL_COLOR,
    FRAME_COLOR,
)


# 主窗口类，用来整合各个功能页面的显示等操作
class SupermarketGUI(tk.Tk):
    def __init__(self, storage: list[dict]):
        super().__init__()


        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.storage = storage

        self.title("超市管理系统")
        self.geometry("900x600")  # 调整窗口大小
        self.configure(bg=BACKGROUND_COLOR)

        # 设置统一的按钮样式
        self.button_style = {
            "bg": BUTTON_COLOR,
            "fg": BUTTON_TEXT_COLOR,
            "font": ("SimSun", 12),
            "width": 20,
            "pady": 5,
            "relief": "raised",
            "cursor": "hand2",  # 鼠标悬停时显示手型
        }

        # 设置统一的标签样式
        self.label_style = {
            "bg": BACKGROUND_COLOR,
            "fg": LABEL_COLOR,
            "font": ("SimSun", 12),
        }

        self.show_home_page_hn()

    def on_closing(self):
        if messagebox.askokcancel("退出", "请确认退出系统"):
            self.destroy()
    def show_home_page_hn(self):
        for widget in self.winfo_children():
            widget.destroy()

        home_frame = tk.Frame(self, bg=BACKGROUND_COLOR)
        home_frame.pack(expand=True, pady=50)

        # 添加系统图标或标题图片
        title_label = tk.Label(
            home_frame,
            text="欢迎登录超市管理系统",
            font=("SimSun", 32, "bold"),
            bg=BACKGROUND_COLOR,
            fg=LABEL_COLOR,
        )
        title_label.pack(pady=30)

        # 美化登录按钮
        login_button = tk.Button(
            home_frame,
            text="管理员登录",
            command=self.show_login_page_hn,
            **self.button_style,
        )
        login_button.pack(pady=20)

    def show_login_page_hn(self):
        for widget in self.winfo_children():
            widget.destroy()

        login_frame = tk.Frame(self, bg=FRAME_COLOR, padx=40, pady=40)
        login_frame.pack(expand=True, pady=100)

        title_label = tk.Label(
            login_frame,
            text="管理员登录",
            font=("SimSun", 24, "bold"),
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
        )
        title_label.pack(pady=20)

        # 用户名输入框
        username_frame = tk.Frame(login_frame, bg=FRAME_COLOR)
        username_frame.pack(fill="x", pady=10)

        username_label = tk.Label(
            username_frame,
            text="账号:",
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
            font=("SimSun", 12),
        )
        username_label.pack(side="left", padx=5)

        self.username_entry = tk.Entry(username_frame, font=("SimSun", 12), width=25)
        self.username_entry.pack(side="left", padx=5)

        # 密码输入框
        password_frame = tk.Frame(login_frame, bg=FRAME_COLOR)
        password_frame.pack(fill="x", pady=10)

        password_label = tk.Label(
            password_frame,
            text="密码:",
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
            font=("SimSun", 12),
        )
        password_label.pack(side="left", padx=5)

        self.password_entry = tk.Entry(
            password_frame, show="*", font=("SimSun", 12), width=25
        )
        self.password_entry.pack(side="left", padx=5)

        # 登录按钮
        login_button = tk.Button(
            login_frame, text="登录", command=self.login_verify_hn, **self.button_style
        )
        login_button.pack(pady=20)

    def login_verify_hn(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if check_login_hn(username, password):
            self.show_main_menu_page_hn()
        else:
            messagebox.showerror("登录失败", "账号或密码错误，请重新输入。")

    def show_main_menu_page_hn(self):
        for widget in self.winfo_children():
            widget.destroy()

        main_menu_frame = tk.Frame(self, bg=BACKGROUND_COLOR)
        main_menu_frame.pack(expand=True, pady=30)

        title_label = tk.Label(
            main_menu_frame,
            text="主菜单",
            font=("SimSun", 24, "bold"),
            bg=BACKGROUND_COLOR,
            fg=LABEL_COLOR,
        )
        title_label.pack(pady=20)

        # 创建按钮网格布局
        button_frame = tk.Frame(main_menu_frame, bg=BACKGROUND_COLOR)
        button_frame.pack(pady=20)

        buttons = [
            ("添加商品", self.show_add_goods_page_hn),
            ("删除商品", self.show_delete_goods_page_hn),
            ("查看商品", self.show_view_goods_page_hn),
            ("商品入库", self.show_goods_warehousing_page_hn),
            ("商品出库", self.show_goods_outbound_page_hn),
            ("修改商品", self.show_modify_goods_page_hn),
            ("搜索商品", self.show_search_goods_page_hn),
            ("退出系统", self.destroy),
        ]

        # 创建4x2的按钮网格
        for i, (text, command) in enumerate(buttons):
            row = i // 2
            col = i % 2
            button = tk.Button(
                button_frame, text=text, command=command, **self.button_style
            )
            button.grid(row=row, column=col, padx=20, pady=10)

    def show_add_goods_page_hn(self):
        for widget in self.winfo_children():
            widget.destroy()

        add_goods_frame = tk.Frame(self, bg=BACKGROUND_COLOR)
        add_goods_frame.pack(expand=True, pady=30)

        title_label = tk.Label(
            add_goods_frame,
            text="添加商品",
            font=("SimSun", 24, "bold"),
            bg=BACKGROUND_COLOR,
            fg=LABEL_COLOR,
        )
        title_label.pack(pady=20)

        # 创建输入框容器
        input_frame = tk.Frame(add_goods_frame, bg=FRAME_COLOR, padx=40, pady=30)
        input_frame.pack(pady=20)

        # 商品名称输入
        name_label = tk.Label(
            input_frame,
            text="商品名称:",
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
            font=("SimSun", 12),
        )
        name_label.pack(pady=(0, 5))
        self.name_entry = tk.Entry(input_frame, font=("SimSun", 12), width=25)
        self.name_entry.pack(pady=(0, 15))

        # 商品价格输入
        price_label = tk.Label(
            input_frame,
            text="商品价格:",
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
            font=("SimSun", 12),
        )
        price_label.pack(pady=(0, 5))
        self.price_entry = tk.Entry(input_frame, font=("SimSun", 12), width=25)
        self.price_entry.pack(pady=(0, 15))

        # 库存数量输入
        quantity_label = tk.Label(
            input_frame,
            text="库存数量:",
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
            font=("SimSun", 12),
        )
        quantity_label.pack(pady=(0, 5))
        self.quantity_entry = tk.Entry(input_frame, font=("SimSun", 12), width=25)
        self.quantity_entry.pack(pady=(0, 15))

        # 按钮容器
        button_frame = tk.Frame(add_goods_frame, bg=BACKGROUND_COLOR)
        button_frame.pack(pady=20)

        # 添加按钮
        add_button = tk.Button(
            button_frame,
            text="添加商品",
            command=self.add_goods_hn,
            **self.button_style,
        )
        add_button.pack(side="left", padx=10)

        # 返回按钮
        back_button = tk.Button(
            button_frame,
            text="返回主菜单",
            command=self.show_main_menu_page_hn,
            **self.button_style,
        )
        back_button.pack(side="left", padx=10)

    def add_goods_hn(self):
        try:
            name = self.name_entry.get()
            if not name:
                messagebox.showerror("错误", "请输入商品名称！")
                return

            price_str = self.price_entry.get()
            if not price_str:
                messagebox.showerror("错误", "请输入商品价格！")
                return

            quantity_str = self.quantity_entry.get()
            if not quantity_str:
                messagebox.showerror("错误", "请输入库存数量！")
                return

            try:
                price = float(price_str)
                if price <= 0:
                    messagebox.showerror("错误", "商品价格必须大于0！")
                    return
            except ValueError:
                messagebox.showerror("错误", "商品价格必须是有效的数字！")
                return

            try:
                quantity = int(quantity_str)
                if quantity <= 0:
                    messagebox.showerror("错误", "库存数量必须大于0！")
                    return
            except ValueError:
                messagebox.showerror("错误", "库存数量必须是整数！")
                return

            # 检查商品名是否已存在
            for good in self.storage:
                if good["商品名称"] == name:
                    messagebox.showerror("错误", "该商品名称已存在！")
                    return

            # 创建新商品字典，使用正确的键名
            good = {
                "商品名称": name,
                "商品价格": str(price),  # 转换为字符串以保持一致性
                "库存数量": str(quantity),  # 转换为字符串以保持一致性
            }

            self.storage.append(good)
            messagebox.showinfo("添加成功", f"商品 {name} 添加成功！")
            self.show_main_menu_page_hn()

        except Exception as e:
            messagebox.showerror("错误", f"添加商品时发生错误：{str(e)}")

    def show_delete_goods_page_hn(self):
        for widget in self.winfo_children():
            widget.destroy()

        delete_frame = tk.Frame(self, bg=BACKGROUND_COLOR)
        delete_frame.pack(expand=True, pady=30)

        title_label = tk.Label(
            delete_frame,
            text="删除商品",
            font=("SimSun", 24, "bold"),
            bg=BACKGROUND_COLOR,
            fg=LABEL_COLOR,
        )
        title_label.pack(pady=20)

        # 创建输入框容器
        input_frame = tk.Frame(delete_frame, bg=FRAME_COLOR, padx=40, pady=30)
        input_frame.pack(pady=20)

        # 商品名称输入
        del_name_label = tk.Label(
            input_frame,
            text="要删除的商品名称:",
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
            font=("SimSun", 12),
        )
        del_name_label.pack(pady=(0, 5))
        self.del_name_entry = tk.Entry(input_frame, font=("SimSun", 12), width=25)
        self.del_name_entry.pack(pady=(0, 15))

        # 按钮容器
        button_frame = tk.Frame(delete_frame, bg=BACKGROUND_COLOR)
        button_frame.pack(pady=20)

        # 删除按钮
        delete_button = tk.Button(
            button_frame,
            text="删除商品",
            command=self.delete_goods_hn,
            **self.button_style,
        )
        delete_button.pack(side="left", padx=10)

        # 返回按钮
        back_button = tk.Button(
            button_frame,
            text="返回主菜单",
            command=self.show_main_menu_page_hn,
            **self.button_style,
        )
        back_button.pack(side="left", padx=10)

    def delete_goods_hn(self):
        del_name = self.del_name_entry.get()

        old_len = len(self.storage)
        self.storage = [
            entry for entry in self.storage if entry["商品名称"] != del_name
        ]

        if len(self.storage) != old_len:
            messagebox.showinfo("删除成功", "商品删除成功！")
        else:
            messagebox.showerror("删除失败", "未找到要删除的商品！")

        self.show_main_menu_page_hn()

    def show_view_goods_page_hn(self):
        for widget in self.winfo_children():
            widget.destroy()

        view_frame = tk.Frame(self, bg=BACKGROUND_COLOR)
        view_frame.pack(expand=True, fill="both", padx=50, pady=30)

        title_label = tk.Label(
            view_frame,
            text="商品列表",
            font=("SimSun", 24, "bold"),
            bg=BACKGROUND_COLOR,
            fg=LABEL_COLOR,
        )
        title_label.pack(pady=20)

        # 创建外层框架，用于放置Canvas和Scrollbar
        outer_frame = tk.Frame(view_frame, bg=FRAME_COLOR)
        outer_frame.pack(fill="both", padx=20, pady=10, expand=True)

        # 创建Canvas
        canvas = tk.Canvas(outer_frame, bg=FRAME_COLOR)
        canvas.pack(side=tk.LEFT, fill="both", expand=True)

        # 创建垂直滚动条
        scrollbar = tk.Scrollbar(outer_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 配置Canvas的滚动条
        canvas.configure(yscrollcommand=scrollbar.set)

        # 创建内部框架，用于放置实际的表格内容，它将被放置在Canvas内
        inner_frame = tk.Frame(canvas, bg=FRAME_COLOR)
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        # 创建表头
        headers = ["商品名称", "商品价格", "库存数量"]
        for i, header in enumerate(headers):
            header_label = tk.Label(
                inner_frame,
                text=header,
                font=("SimSun", 12, "bold"),
                bg=FRAME_COLOR,
                fg=LABEL_COLOR,
                width=20,
                pady=10,
            )
            header_label.grid(row=0, column=i, sticky="ew")

        # 显示商品数据
        if not self.storage:
            no_data_label = tk.Label(
                inner_frame,
                text="暂无商品数据",
                font=("SimSun", 11),
                bg=FRAME_COLOR,
                fg=LABEL_COLOR,
                pady=20,
            )
            no_data_label.grid(row=1, column=0, columnspan=3)
        else:
            for row_idx, good in enumerate(self.storage, 1):
                # 商品名称
                tk.Label(
                    inner_frame,
                    text=good["商品名称"],
                    font=("SimSun", 11),
                    bg=FRAME_COLOR,
                    width=20,
                    pady=5,
                ).grid(row=row_idx, column=0)

                # 商品价格
                tk.Label(
                    inner_frame,
                    text=f"¥{float(good['商品价格']):.2f}",
                    font=("SimSun", 11),
                    bg=FRAME_COLOR,
                    width=20,
                    pady=5,
                ).grid(row=row_idx, column=1)

                # 库存数量
                tk.Label(
                    inner_frame,
                    text=str(good["库存数量"]),
                    font=("SimSun", 11),
                    bg=FRAME_COLOR,
                    width=20,
                    pady=5,
                ).grid(row=row_idx, column=2)

        # 更新Canvas的滚动区域，使其能正确滚动
        inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        # 返回按钮容器
        button_frame = tk.Frame(view_frame, bg=BACKGROUND_COLOR)
        button_frame.pack(pady=20)

        # 返回按钮
        back_button = tk.Button(
            button_frame,
            text="返回主菜单",
            command=self.show_main_menu_page_hn,
            **self.button_style,
        )
        back_button.pack()

    def show_goods_warehousing_page_hn(self):
        for widget in self.winfo_children():
            widget.destroy()

        warehousing_frame = tk.Frame(self, bg=BACKGROUND_COLOR)
        warehousing_frame.pack(expand=True, pady=30)

        title_label = tk.Label(
            warehousing_frame,
            text="商品入库",
            font=("SimSun", 24, "bold"),
            bg=BACKGROUND_COLOR,
            fg=LABEL_COLOR,
        )
        title_label.pack(pady=20)

        # 创建输入框容器
        input_frame = tk.Frame(warehousing_frame, bg=FRAME_COLOR, padx=40, pady=30)
        input_frame.pack(pady=20)

        # 商品名称输入
        name_label = tk.Label(
            input_frame,
            text="商品名称:",
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
            font=("SimSun", 12),
        )
        name_label.pack(pady=(0, 5))

        self.name_entry_warehousing = tk.Entry(
            input_frame, font=("SimSun", 12), width=25
        )
        self.name_entry_warehousing.pack(pady=(0, 15))

        # 入库数量输入
        quantity_label = tk.Label(
            input_frame,
            text="入库数量:",
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
            font=("SimSun", 12),
        )
        quantity_label.pack(pady=(0, 5))

        self.quantity_entry_warehousing = tk.Entry(
            input_frame, font=("SimSun", 12), width=25
        )
        self.quantity_entry_warehousing.pack(pady=(0, 15))

        # 按钮容器
        button_frame = tk.Frame(warehousing_frame, bg=BACKGROUND_COLOR)
        button_frame.pack(pady=20)

        # 入库按钮
        warehousing_button = tk.Button(
            button_frame,
            text="确认入库",
            command=self.goods_warehousing_hn,
            **self.button_style,
        )
        warehousing_button.pack(side="left", padx=10)

        # 返回按钮
        back_button = tk.Button(
            button_frame,
            text="返回主菜单",
            command=self.show_main_menu_page_hn,
            **self.button_style,
        )
        back_button.pack(side="left", padx=10)

    def goods_warehousing_hn(self):
        name = self.name_entry_warehousing.get()
        quantity = int(self.quantity_entry_warehousing.get())

        for good in self.storage:
            if good["商品名称"] == name:
                current_quantity = int(good["库存数量"])  # 将字符串转换为整数
                good["库存数量"] = str(current_quantity + quantity)  # 转回字符串保存
                messagebox.showinfo("入库成功", "商品入库操作完成")
                break
        else:  # 如果循环正常结束（没有找到商品）
            messagebox.showerror("入库失败", "未找到该商品！")
        self.show_main_menu_page_hn()

    def show_goods_outbound_page_hn(self):
        for widget in self.winfo_children():
            widget.destroy()

        outbound_frame = tk.Frame(self, bg=BACKGROUND_COLOR)
        outbound_frame.pack(expand=True, pady=30)

        title_label = tk.Label(
            outbound_frame,
            text="商品出库",
            font=("SimSun", 24, "bold"),
            bg=BACKGROUND_COLOR,
            fg=LABEL_COLOR,
        )
        title_label.pack(pady=20)

        # 创建输入框容器
        input_frame = tk.Frame(outbound_frame, bg=FRAME_COLOR, padx=40, pady=30)
        input_frame.pack(pady=20)

        # 商品名称输入
        name_label = tk.Label(
            input_frame,
            text="商品名称:",
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
            font=("SimSun", 12),
        )
        name_label.pack(pady=(0, 5))

        self.name_entry_outbound = tk.Entry(input_frame, font=("SimSun", 12), width=25)
        self.name_entry_outbound.pack(pady=(0, 15))

        # 出库数量输入
        quantity_label = tk.Label(
            input_frame,
            text="出库数量:",
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
            font=("SimSun", 12),
        )
        quantity_label.pack(pady=(0, 5))

        self.quantity_entry_outbound = tk.Entry(
            input_frame, font=("SimSun", 12), width=25
        )
        self.quantity_entry_outbound.pack(pady=(0, 15))

        # 按钮容器
        button_frame = tk.Frame(outbound_frame, bg=BACKGROUND_COLOR)
        button_frame.pack(pady=20)

        # 出库按钮
        outbound_button = tk.Button(
            button_frame,
            text="确认出库",
            command=self.goods_outbound_hn,
            **self.button_style,
        )
        outbound_button.pack(side="left", padx=10)

        # 返回按钮
        back_button = tk.Button(
            button_frame,
            text="返回主菜单",
            command=self.show_main_menu_page_hn,
            **self.button_style,
        )
        back_button.pack(side="left", padx=10)

    def goods_outbound_hn(self):
        try:
            name = self.name_entry_outbound.get()
            if not name:
                messagebox.showerror("错误", "请输入商品名称！")
                return

            quantity_str = self.quantity_entry_outbound.get()
            if not quantity_str:
                messagebox.showerror("错误", "请输入出库数量！")
                return

            quantity = int(quantity_str)
            if quantity <= 0:
                messagebox.showerror("错误", "出库数量必须大于0！")
                return

            # 修复类型转换问题
            for good in self.storage:
                if good["商品名称"] == name:
                    current_quantity = int(good["库存数量"])  # 将字符串转换为整数
                    if current_quantity >= quantity:
                        good["库存数量"] = str(
                            current_quantity - quantity
                        )  # 转回字符串保存
                        messagebox.showinfo(
                            "出库成功", f"商品出库成功！\n当前库存：{good['库存数量']}"
                        )
                    else:
                        messagebox.showerror(
                            "出库失败", f"库存不足！当前库存：{current_quantity}"
                        )
                    break
            else:  # 如果循环正常结束（没有找到商品）
                messagebox.showerror("出库失败", "未找到该商品！")

        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字！")
        except Exception as e:
            messagebox.showerror("错误", f"发生错误：{str(e)}")

    def show_modify_goods_page_hn(self):
        for widget in self.winfo_children():
            widget.destroy()

        modify_frame = tk.Frame(self, bg=BACKGROUND_COLOR)
        modify_frame.pack(expand=True, pady=30)

        title_label = tk.Label(
            modify_frame,
            text="修改商品",
            font=("SimSun", 24, "bold"),
            bg=BACKGROUND_COLOR,
            fg=LABEL_COLOR,
        )
        title_label.pack(pady=20)

        # 创建输入框容器
        input_frame = tk.Frame(modify_frame, bg=FRAME_COLOR, padx=40, pady=30)
        input_frame.pack(pady=20)

        # 要修改的商品名称输入
        name_label = tk.Label(
            input_frame,
            text="要修改的商品名称:",
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
            font=("SimSun", 12),
        )
        name_label.pack(pady=(0, 5))

        self.name_entry_modify = tk.Entry(input_frame, font=("SimSun", 12), width=25)
        self.name_entry_modify.pack(pady=(0, 15))

        # 新商品名称输入
        new_name_label = tk.Label(
            input_frame,
            text="新商品名称（可不填）:",
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
            font=("SimSun", 12),
        )
        new_name_label.pack(pady=(0, 5))

        self.new_name_entry = tk.Entry(input_frame, font=("SimSun", 12), width=25)
        self.new_name_entry.pack(pady=(0, 15))

        # 新商品价格输入
        new_price_label = tk.Label(
            input_frame,
            text="新商品价格（可不填）:",
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
            font=("SimSun", 12),
        )
        new_price_label.pack(pady=(0, 5))

        self.new_price_entry = tk.Entry(input_frame, font=("SimSun", 12), width=25)
        self.new_price_entry.pack(pady=(0, 15))

        # 新库存数量输入
        new_quantity_label = tk.Label(
            input_frame,
            text="新库存数量（可不填）:",
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
            font=("SimSun", 12),
        )
        new_quantity_label.pack(pady=(0, 5))

        self.new_quantity_entry = tk.Entry(input_frame, font=("SimSun", 12), width=25)
        self.new_quantity_entry.pack(pady=(0, 15))

        # 按钮容器
        button_frame = tk.Frame(modify_frame, bg=BACKGROUND_COLOR)
        button_frame.pack(pady=20)

        # 修改按钮
        modify_button = tk.Button(
            button_frame,
            text="确认修改",
            command=self.modify_goods_hn,
            **self.button_style,
        )
        modify_button.pack(side="left", padx=10)

        # 返回按钮
        back_button = tk.Button(
            button_frame,
            text="返回主菜单",
            command=self.show_main_menu_page_hn,
            **self.button_style,
        )
        back_button.pack(side="left", padx=10)

    def modify_goods_hn(self):
        try:
            name = self.name_entry_modify.get()
            if not name:
                messagebox.showerror("错误", "请输入要修改的商品名称！")
                return

            new_name = self.new_name_entry.get()
            new_price = self.new_price_entry.get()
            new_quantity = self.new_quantity_entry.get()

            if not (new_name or new_price or new_quantity):
                messagebox.showerror("错误", "请至少填写一项要修改的内容！")
                return

            found = False
            for good in self.storage:
                if good["商品名称"] == name:
                    found = True
                    if new_name:
                        good["商品名称"] = new_name
                    if new_price:
                        try:
                            good["商品价格"] = str(float(new_price))
                        except ValueError:
                            messagebox.showerror("错误", "商品价格必须是有效的数字！")
                            return
                    if new_quantity:
                        try:
                            good["库存数量"] = str(int(new_quantity))
                        except ValueError:
                            messagebox.showerror("错误", "库存数量必须是整数！")
                            return
                    break

            if not found:
                messagebox.showerror("错误", "未找到要修改的商品！")
                return

            messagebox.showinfo("修改成功", "商品修改成功！")
            self.show_main_menu_page_hn()

        except Exception as e:
            messagebox.showerror("错误", f"修改时发生错误：{str(e)}")

    def show_search_goods_page_hn(self):
        for widget in self.winfo_children():
            widget.destroy()

        search_frame = tk.Frame(self, bg=BACKGROUND_COLOR)
        search_frame.pack(expand=True, pady=30)

        title_label = tk.Label(
            search_frame,
            text="搜索商品",
            font=("SimSun", 24, "bold"),
            bg=BACKGROUND_COLOR,
            fg=LABEL_COLOR,
        )
        title_label.pack(pady=20)

        # 创建输入框容器
        input_frame = tk.Frame(search_frame, bg=FRAME_COLOR, padx=40, pady=30)
        input_frame.pack(pady=20)

        # 搜索输入框
        search_name_label = tk.Label(
            input_frame,
            text="请输入要搜索的商品名称:",
            bg=FRAME_COLOR,
            fg=LABEL_COLOR,
            font=("SimSun", 12),
        )
        search_name_label.pack(pady=(0, 5))

        self.search_name_entry = tk.Entry(input_frame, font=("SimSun", 12), width=25)
        self.search_name_entry.pack(pady=(0, 15))

        # 按钮容器
        button_frame = tk.Frame(search_frame, bg=BACKGROUND_COLOR)
        button_frame.pack(pady=20)

        # 搜索按钮
        search_button = tk.Button(
            button_frame,
            text="搜索商品",
            command=self.search_goods_hn,
            **self.button_style,
        )
        search_button.pack(side="left", padx=10)

        # 返回按钮
        back_button = tk.Button(
            button_frame,
            text="返回主菜单",
            command=self.show_main_menu_page_hn,
            **self.button_style,
        )
        back_button.pack(side="left", padx=10)

    def search_goods_hn(self):
        try:
            search_name = self.search_name_entry.get()
            if not search_name:
                messagebox.showerror("错误", "请输入要搜索的商品名称！")
                return

            # 完善搜索商品逻辑，查找匹配商品并展示等操作
            found_goods = []
            for good in self.storage:
                if search_name in good["商品名称"]:
                    found_goods.append(good)

            if found_goods:
                result_text = "搜索结果：\n\n"
                for good in found_goods:
                    result_text += f"商品名称: {good['商品名称']}\n"
                    result_text += f"商品价格: ¥{float(good['商品价格']):.2f}\n"
                    result_text += f"库存数量: {good['库存数量']}\n"
                    result_text += "-" * 30 + "\n"
                messagebox.showinfo("搜索结果", result_text)
            else:
                messagebox.showinfo("搜索结果", "未找到匹配的商品")

        except Exception as e:
            messagebox.showerror("错误", f"搜索时发生错误：{str(e)}")
