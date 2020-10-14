class AnonymousSurvey:

    def __init__(self,question):
        self.question = question
        self.responses = []


    def show_question(self):
        print(f'Ответьте на вопрос: {self.question}')


    def add_answer(self,new_answer):
        self.responses.append(new_answer)


    def show_answers(self):
        for answer in self.responses:
            print(f' {answer}')
