# Generating dummy data
set.seed(123)  # Setting seed for reproducibility
n <- 100  # Number of observations
x1 <- rnorm(n, mean = 50, sd = 10)  # Independent variable 1 (normally distributed)
x2 <- rnorm(n, mean = 30, sd = 5)   # Independent variable 2 (normally distributed)
epsilon <- rnorm(n, mean = 0, sd = 3)  # Error term (normally distributed with mean 0, sd 3)
y <- 10 + 2*x1 - 3*x2 + epsilon  # Dependent variable (linear relationship with x1 and x2)

# Creating a data frame
dummy_data <- data.frame(y = y, x1 = x1, x2 = x2)

# Perform linear regression
lm_model <- lm(y ~ x1 + x2, data = dummy_data)

# Summary of the regression results
summary(lm_model)

# Predicting values using the model
predicted_values <- predict(lm_model, dummy_data)

# Plotting actual vs. predicted values
plot(dummy_data$y, predicted_values, main = "Actual vs. Predicted", 
     xlab = "Actual Y", ylab = "Predicted Y")
abline(0, 1, col = "red")  # Adding a 45-degree line for comparison

