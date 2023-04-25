from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quizz_brain: QuizBrain):
        self.quiz = quizz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text=f"{self.quiz.score}", bg=THEME_COLOR)
        self.score.grid(column=1, row=0, pady=20, padx=20)
        self.my_canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.my_canvas.create_text(
            150, 125,
            width=250,
            text="THE QUESTION",
            fill="black",
            font=("arial", 20, 'italic')
        )
        self.my_canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, highlightcolor=THEME_COLOR, command=self.true_pressed)
        self.false_button.grid(column=1, row=2)
        self.true_button = Button(image=true_image, highlightthickness=0, highlightcolor=THEME_COLOR, command=self.false_pressed)
        self.true_button.grid(column=0, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.my_canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.my_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.my_canvas.config(bg="white")
            self.my_canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.my_canvas.config(bg="green")
        elif not is_right:
            self.my_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)




