'''44 Bank Loan Approval:
Implement a program to simulate a bank loan approval system. Consider factors such as credit score, income, and loan amount. Use nested if statements to determine whether the loan should be approved, rejected, or needs further evaluation.
'''


credit_score = int(input("Enter your credit score: "))
income = float(input("Enter your income: "))
loan_amount = float(input("Enter the loan amount: "))



if credit_score >= 700 and income >= 50000 and loan_amount <= 100000:
    print("Loan approved!")
elif credit_score >= 600 and income >= 40000 and loan_amount <= 80000:
    print("Loan approved with further evaluation.")
else:
    print("Loan rejected.")
