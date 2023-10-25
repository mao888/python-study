"""
5.参考单词练习系统，设计一个学生成绩管理系统。
"""
"""
一个学生成绩管理系统可以用于记录学生的成绩、计算平均分、查看学生信息等。以下是一个简单的学生成绩管理系统的设计，包括界面设计、成绩记录、计算平均分、错误处理等方面的内容：
"""
import tkinter
import tkinter.messagebox


class StudentGradeManagement:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('400x300')
        self.root.title('学生成绩管理系统')
        self.students = []

        # 添加学生信息的界面元素
        self.label_name = tkinter.Label(self.root, text='姓名：')
        self.label_score = tkinter.Label(self.root, text='成绩：')
        self.entry_name = tkinter.Entry(self.root)
        self.entry_score = tkinter.Entry(self.root)
        self.add_button = tkinter.Button(self.root, text='添加学生', command=self.add_student)

        # 显示学生信息的界面元素
        self.display_text = tkinter.Text(self.root, height=10, width=40)

        # 计算平均分的按钮
        self.average_button = tkinter.Button(self.root, text='计算平均分', command=self.calculate_average)

        self.layout_interface()

    def layout_interface(self):
        # 添加学生信息界面布局
        self.label_name.pack()
        self.entry_name.pack()
        self.label_score.pack()
        self.entry_score.pack()
        self.add_button.pack()

        # 显示学生信息界面布局
        self.display_text.pack()

        # 计算平均分按钮布局
        self.average_button.pack()

    def add_student(self):
        name = self.entry_name.get()
        score = self.entry_score.get()
        if name and score:
            try:
                score = float(score)
                self.students.append({'name': name, 'score': score})
                self.display_student_info()
                self.entry_name.delete(0, 'end')
                self.entry_score.delete(0, 'end')
            except ValueError:
                tkinter.messagebox.showerror('错误', '成绩必须是数字')
        else:
            tkinter.messagebox.showerror('错误', '请填写姓名和成绩')

    def display_student_info(self):
        self.display_text.delete(1.0, 'end')
        for student in self.students:
            self.display_text.insert('end', f"姓名: {student['name']}, 成绩: {student['score']}\n")

    def calculate_average(self):
        if self.students:
            total_score = sum([student['score'] for student in self.students])
            average_score = total_score / len(self.students)
            tkinter.messagebox.showinfo('平均分', f'平均分为：{average_score:.2f}')
        else:
            tkinter.messagebox.showinfo('平均分', '没有学生信息')


if __name__ == "__main__":
    app = StudentGradeManagement()
    app.root.mainloop()

"""
这个简单的学生成绩管理系统允许用户输入学生姓名和成绩，添加学生信息，显示学生信息，以及计算平均分。错误处理机制用于确保输入的成绩是数字，同时也要求用户填写姓名和成绩。界面中使用了Tkinter库，但你可以根据需要进行美化和扩展。

要扩展这个系统，你可以考虑添加以下功能：

存储学生信息：将学生信息保存到文件或数据库中，以便在下次打开应用程序时加载。
成绩分析：计算最高分、最低分、成绩分布等统计信息。
成绩编辑和删除：允许用户编辑和删除学生信息。
数据可视化：使用图表或图形来显示成绩数据。
用户认证和权限：添加用户登录和权限控制，以保护敏感数据。
错误处理：更全面的错误处理和反馈机制，以提高用户体验。
"""