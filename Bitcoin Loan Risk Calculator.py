import numpy as np


def bitcoin_loan_risk_calculator(
        loan_amount,
        interest_rate,
        loan_term_years,
        current_bitcoin_price,
        expected_annual_return,
        volatility,
        simulations=10000
):
    # Monthly calculations
    monthly_rate = interest_rate / 12 / 100
    num_months = loan_term_years * 12
    monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** num_months) / (
                (1 + monthly_rate) ** num_months - 1)

    # Convert annual to monthly rate
    monthly_return = (1 + expected_annual_return) ** (1 / 12) - 1
    monthly_volatility = volatility / np.sqrt(12)

    # Initialize array for simulation results
    final_values = np.zeros(simulations)

    # Run Monte Carlo simulation
    for i in range(simulations):
        bitcoin_value = loan_amount / current_bitcoin_price
        for _ in range(num_months):
            # Simulate Bitcoin price movement
            bitcoin_value *= np.exp(
                np.random.normal(monthly_return - 0.5 * monthly_volatility ** 2, monthly_volatility))
            # Subtract monthly payment
            bitcoin_value -= monthly_payment / (bitcoin_value * current_bitcoin_price)
        final_values[i] = bitcoin_value * current_bitcoin_price - loan_amount

    # Calculate risk metrics
    expected_profit = np.mean(final_values)
    probability_of_loss = np.sum(final_values < 0) / simulations
    var_95 = np.percentile(final_values, 5)

    return {
        "Expected Profit": expected_profit,
        "Probability of Loss": probability_of_loss,
        "95% VaR": -var_95
    }


# Example usage
result = bitcoin_loan_risk_calculator(
    loan_amount=10000,
    interest_rate=5,
    loan_term_years=3,
    current_bitcoin_price=50000,
    expected_annual_return=0.20,
    volatility=0.60,
    simulations=10000
)

print(result)