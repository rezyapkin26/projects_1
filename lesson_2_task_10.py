def bank(X, Y):
    rate = 0.10  # 10% годовых
    return X * (1 + rate) ** Y  # формула подсчета

initial_deposit = 10000  # X рублей
years = 5  # Y лет
future_value = bank(initial_deposit, years)
print(f"Сумма на счете спустя {years} лет: {future_value:.2f} рублей")