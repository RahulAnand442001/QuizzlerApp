from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Ariel", 15, "bold")


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=50, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=FONT)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Some text is here",
                                                     font=FONT, width=280, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.f_photo = PhotoImage(file="images/false.png")
        self.r_photo = PhotoImage(file="images/true.png")
        self.false_btn = Button(image=self.f_photo, bg=THEME_COLOR, borderwidth=0, command=self.False_pressed)
        self.true_btn = Button(image=self.r_photo, bg=THEME_COLOR, borderwidth=0, command=self.True_pressed)
        self.false_btn.grid(row=2, column=0)
        self.true_btn.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="QUIZ OVER", fill="blue")
            self.false_btn.config(state="disable")
            self.true_btn.config(state="disable")

    def True_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def False_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_next_question)
