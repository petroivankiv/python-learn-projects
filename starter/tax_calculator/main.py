import customtkinter as ctk

class TaxCalculator:
    def __init__(self) -> None:
        # initialize window
        self.window = ctk.CTk()
        self.window.title('Обчислення податку')
        self.window.geometry('280x200')
        self.window.resizable(False, False)
        
        self.padding: dict = {'padx': 10, 'pady': 10}
        
        # income label and entry
        self.income_label = ctk.CTkLabel(self.window, text='Прибуток:')
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)
        
        # Tax label and entry
        self.tax_rate_label = ctk.CTkLabel(self.window, text='Відсоток:')
        self.tax_rate_label.grid(row=1, column=0, **self.padding)
        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)
        
        # Result label and entry
        self.result_label = ctk.CTkLabel(self.window, text='Податок:')
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.grid(row=2, column=1, **self.padding)
        self.result_entry.insert(0, '0')
        
        # button
        self.calculate_btn = ctk.CTkButton(self.window, command=self.calculate)
        self.calculate_btn.grid(row=3, column=1, **self.padding)
        
        
    def update_result(self, text: str):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)
        
    def calculate(self):
        try:
            income: float = float(self.income_entry.get())
            tax_rate: float = float(self.tax_rate_entry.get())
            self.update_result(f'UAH{income * (tax_rate / 100):,.2f}')
        except ValueError as e:
            print(f'Помилка: {e}')
            self.update_result('Неправильне значення')
        
    
    def run(self):
        self.window.mainloop()
        
        
if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()