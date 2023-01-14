library(scatterD3)
mydata<-read.csv('diseases.csv')
scatterD3(data = mydata, x = x, y = y, lab = label,
          #col_var = cyl, symbol_var = am,
          xlab = "X", ylab = "Y", #col_lab = "Cylinders",
          symbol_lab = "GHDx", lasso = TRUE)

# mtcars$names <- rownames(mtcars)
# scatterD3(data = mtcars, x = wt, y = mpg, lab = names,
#           col_var = cyl, symbol_var = am,
#           xlab = "Weight", ylab = "Mpg", col_lab = "Cylinders",
#           symbol_lab = "Manual transmission")
