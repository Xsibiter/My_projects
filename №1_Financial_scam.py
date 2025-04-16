from tkinter import *

class LoanCalculator:
    def __init__(self):
        root = Tk()
        root.geometry("500x300")
        root.title("Кредитный калькулятор")
        root.config(bg='#a39ea0')

        Label(root, text="Годовая ставка, %", font=('Arial', 15, 'bold'), bg='#a39ea0').place(x=10, y=10)
        Label(root, text="Срок, лет", font=('Arial', 15, 'bold'), bg='#a39ea0').place(x=10, y=50)
        Label(root, text="Сумма кредита", font=('Arial', 15, 'bold'), bg='#a39ea0').place(x=10, y=90)
        Label(root, text="Ежемесячный платёж:", font=('Arial', 15, 'bold'), bg='#a39ea0').place(x=10, y=150)
        Label(root, text="Общая сумма выплаты:", font=('Arial', 15, 'bold'), bg='#a39ea0').place(x=10, y=190)

        self.annualinterestVar = StringVar()
        Entry(root, textvariable=self.annualinterestVar, font=('Arial', 15, 'bold')).place(x=220, y=10)

        self.numberofyearsVar = StringVar()
        Entry(root, textvariable=self.numberofyearsVar, font=('Arial', 15, 'bold')).place(x=220, y=50)

        self.loanamountVar = StringVar()
        Entry(root, textvariable=self.loanamountVar, font=('Arial', 15, 'bold')).place(x=220, y=90)

        self.monthlypaymentVar = StringVar()
        Label(root, textvariable=self.monthlypaymentVar, font=('Arial', 15, 'bold'), bg='#a39ea0').place(x=220, y=150)

        self.totalpaymentVar = StringVar()
        Label(root, textvariable=self.totalpaymentVar, font=('Arial', 15, 'bold'), bg='#a39ea0').place(x=220, y=190)

        Button(root, text="Рассчитать", font=('Arial', 15, 'bold'), command=self.calculateloan).place(x=180, y=240)

        root.mainloop()

    def calculateloan(self):
        try:
            loan_amount = float(self.loanamountVar.get())
            annual_interest_rate = float(self.annualinterestVar.get())
            number_of_years = int(self.numberofyearsVar.get())

            monthly_interest_rate = annual_interest_rate / 1200
            monthly_payment = self.getmonthlyPayment(loan_amount, monthly_interest_rate, number_of_years)
            total_payment = monthly_payment * 12 * number_of_years

            self.monthlypaymentVar.set(f"{monthly_payment:.2f}")
            self.totalpaymentVar.set(f"{total_payment:.2f}")
        except ValueError:
            self.monthlypaymentVar.set("Ошибка")
            self.totalpaymentVar.set("Ошибка")

    def getmonthlyPayment(self, loan_amount, monthly_interest_rate, number_of_years):
        monthly_payment = loan_amount * monthly_interest_rate / (1 - 1 / (1 + monthly_interest_rate) ** (number_of_years * 12))
        return monthly_payment

LoanCalculator()